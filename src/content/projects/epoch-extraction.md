---
title: Epoch Extraction for Speaker Differentiation
summary: Speech signal analysis using zero-frequency filtering and a locking-based comparison method, with an implementation path toward Raspberry Pi and hardware-oriented systems.
year: 2024
status: completed
researchArea: Signal processing
methods: [Zero Frequency Filtering, epoch extraction, speaker differentiation, MATLAB, embedded implementation]
datasets: [Recorded speech from six speakers]
results:
  - The associated preprint reports an average Delta of 7.5 for the reference speaker and lower values for different speakers.
  - The reported comparison corresponds to an approximately 73% reduction in similar epoch positions for different speakers.
role: Co-author; contributed to filtering, epoch extraction, speaker comparison, evaluation, and implementation-oriented analysis.
collaborators: [Daniel Ferro, Xu Zhao, Abdul Jabbar Syed, Anil K. Vuppala, Azeemuddin Syed]
featured: true
cover: /assets/projects/epoch-extraction.png
sortOrder: 40
links:
  paper: https://arxiv.org/abs/2407.18447
  demo: https://www.youtube.com/watch?v=1KFswKUuh5Y
---

## Problem

An epoch, or glottal closure instant, is an important event in voiced speech. Detecting these events reliably can support speech analysis and speaker comparison, but the source signal is affected by the time-varying vocal tract system.

## Approach

The work compared zero-frequency filtering methods and used a locking-based procedure to count epoch locations that aligned with a reference speaker. The project also considered implementation constraints beyond desktop analysis.

## Research output

The resulting paper is available as an arXiv preprint. Its reported experiment used six speakers and should be interpreted within that evaluation scope.
