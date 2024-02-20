#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 19:28:41 2024

@author: wdyrka
"""

import pandas as pd
import matplotlib.pyplot as plt

fass = pd.read_csv('fass_ntm_domain_test_coord_vs_pcfg_comb.csv', sep='\t',
                   header=None)
fass.loc[fass[5] < 0, 5] = 0

bass = pd.read_csv('bass_ntm_domain_test_coord_vs_pcfg_comb.csv', sep='\t',
                   header=None)
bass.loc[bass[5] < 0, 5] = 0


print(bass)

col = 5

print(bass[col].describe())
print(fass[col].describe())

plt.violinplot([bass[col], fass[col]])
plt.xticks([1, 2], ['bass', 'fass'])
plt.title('motif coverage (pcfg comb)')
