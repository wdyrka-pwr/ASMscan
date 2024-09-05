import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from cycler import cycler
from typing import Tuple, List
import os

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path, sep="\t")

def create_scatter_plot(ax: plt.Axes, data: pd.DataFrame, title: str, score_threshold: float) -> None:
    groups = data.groupby("dataset")
    color_cycle = plt.cm.rainbow(np.linspace(0, 1, len(groups)))
    ax.set_prop_cycle(cycler(color=color_cycle))

    for name, dset in groups:
        above_threshold = dset[dset['prob'] >= score_threshold]
        below_threshold = dset[dset['prob'] < score_threshold]
        
        ax.scatter(above_threshold["umap_x"], above_threshold["umap_y"],
                   label=f"{name} (n={len(dset)})", s=10, alpha=1.0, marker='o')
        ax.scatter(below_threshold["umap_x"], below_threshold["umap_y"],
                   s=10, alpha=0.2, marker='x', color=ax._get_lines.get_next_color())

    ax.set_title(title)
    if "ProteinBERT" in title:
        ax.set_xlabel("UMAP X")
        ax.set_ylabel("UMAP Y")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

def create_retention_plot(ax: plt.Axes, data: pd.DataFrame, score_threshold: float, title: str) -> None:
    total_counts = data.groupby("dataset").size()
    filtered_counts = data[data['prob'] >= score_threshold].groupby("dataset").size()
    retention_percentages = (filtered_counts / total_counts * 100).round(2)

    bars = retention_percentages.plot(kind='bar', ax=ax, color=plt.cm.rainbow(np.linspace(0, 1, len(retention_percentages))))
    ax.set_title(title)
    ax.set_ylim(0, 100)
    
    if "ProteinBERT" in title:
        ax.set_xlabel("Datasets")
        ax.set_ylabel("Retention %")
    else:
        ax.set_xlabel("")

    ax.set_xticks(range(len(retention_percentages)))
    ax.set_xticklabels(retention_percentages.index, rotation=45, ha='right')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    for i, v in enumerate(retention_percentages):
        ax.text(i, v + 1, f'{v}%', ha='center', va='bottom', fontweight='bold')

    ax.yaxis.grid(True, linestyle='--', alpha=0.7)

def create_plot(path_pbert: str, path_lstm: str, score_threshold: float = 0.5, figsize: Tuple[int, int] = (8, 6)) -> Tuple[plt.Figure, List[plt.Axes]]:
    data_pbert = load_data(path_pbert)
    data_lstm = load_data(path_lstm)

    fig, axes = plt.subplots(2, 2, figsize=(figsize[0]*2, figsize[1]*2))
    axes = axes.flatten()

    create_scatter_plot(axes[0], data_pbert, "ProteinBERT", score_threshold)
    create_scatter_plot(axes[1], data_lstm, "LSTM", score_threshold)

    create_retention_plot(axes[2], data_pbert, score_threshold, "")
    create_retention_plot(axes[3], data_lstm, score_threshold, "")

    handles, labels = [], []
    for ax in axes[:2]:
        h, l = ax.get_legend_handles_labels()
        handles.extend(h)
        labels.extend(l)

    handles, labels = axes[0].get_legend_handles_labels()
    
    fig.legend(handles, labels, loc='upper center', ncol=len(labels)//2, bbox_to_anchor=(0.5, 1.06), title="Datasets")

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.15)
    plt.savefig("comparison_plot_thr" + str(score_threshold) + ".png", dpi=600, bbox_inches='tight')
    return fig, axes

if __name__ == "__main__":
    for folder in os.listdir("."):
        print(folder)
        if os.path.isdir(folder):
            os.chdir(folder)
            create_plot(path_lstm="lstm.csv", path_pbert="pbert.csv", score_threshold=0.5)
            os.chdir("..")