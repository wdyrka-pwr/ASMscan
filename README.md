# ASMscan
This repository keeps data, models, scripts and results for the manuscript *Deep discriminative models in the detection of amyloid signaling motifs* by Krzysztof Pysz, Jakub Gałązka & Witold Dyrka. 

## Abstract
Amyloid signaling sequences adopt the cross-β fold that is capable of self-replication in the templating process. Propagation of the amyloid fold from the receptor to the effector protein is used for signal transduction in the immune response pathways in animals, fungi and bacteria. So far, a dozen of families of amyloid signaling motifs (ASMs) have been classified. Unfortunately, due to the wide variety of ASMs it is difficult to identify them in large protein databases available, which limits the possibility of conducting experimental studies.

To date, various deep learning (DL) models have been applied across a range of protein-related tasks, including domain family classification and the prediction of protein structure and protein-protein interactions. In this study, we develop tailor-made bidirectional LSTM and BERT-based architectures to model ASM, and compare their performance against a state-of-the-art machine learning grammatical model.

Our research is focused on developing a discriminative model of generalized amyloid signaling motifs, capable of detecting ASMs in large data sets. The DL-based models are trained on a diverse set of motif families and a global negative set, and used to identify ASMs from remotely related families. We investigate the differences in data representation in both models in order to identify potentially amyloidogenic fragments and find that our DL-based models are well suited for ASM detection tasks and often outperform the previous grammatical model.

## Source code for models
The source code for the models used in this study is available from the following repositories:
* PCFG: git.e-science.pl/wdyrka/pcfg-cm,
* ASMScan-BiLSTM: github.com/jakub-galazka/asmscan-bilstm,
* ASMScan-ProteinBERT: github.com/chrispysz/asmscan-proteinbert.

## Try it out
Ready-to-use implementations of the neural network models are available via:
* ASMScan-BiLSTM: pypi.org/project/asmscan-bilstm/ (Python package),
* ASMScan-ProteinBERT: github.com/chrispysz/asmscan-proteinbert-run (Docker image).

## Contact
Please contact **witold** dot **dyrka** at **pwr** dot **edu** dot **pl**.
