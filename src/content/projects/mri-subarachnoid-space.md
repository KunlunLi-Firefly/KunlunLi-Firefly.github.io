---
title: Subarachnoid Space Analysis in Brain MRI
summary: A multi-stage MRI analysis workflow covering image registration, ventricle segmentation, cross-contrast synthesis, and subarachnoid space volume estimation.
year: 2024
status: coursework
researchArea: Medical imaging
methods: [FSL registration, FastSurfer, CycleGAN, K-means clustering, mathematical morphology]
datasets: [T1-weighted MRI, T2-weighted MRI, MNI space]
results:
  - Produced registered MRI volumes in standardized MNI space.
  - Used FastSurfer segmentations to support ventricle and Evans ratio analysis.
  - Explored T1-to-T2 synthesis and a classical image-processing pipeline for SAS estimation.
role: Course project work across registration, segmentation, image synthesis, and quantitative measurement.
collaborators: []
featured: false
cover: /assets/projects/mri-analysis.png
sortOrder: 30
links:
  repository: https://github.com/KunlunLi-Firefly/MRI_SAS
---

## Problem

Quantitative analysis of brain MRI often requires several dependent steps: spatial alignment, anatomical segmentation, contrast handling, and measurement. Errors in one stage can propagate through the rest of the pipeline.

## Approach

The project registered T1- and T2-weighted scans to a 1 mm MNI reference space, applied FastSurfer for anatomical segmentation, explored CycleGAN-based cross-contrast synthesis, and investigated subarachnoid space estimation using clustering, region growing, and morphology.

## Scope

The work is presented as a course project and technical exploration. The available report emphasizes workflow construction and qualitative evaluation; it does not support a clinical validation claim.
