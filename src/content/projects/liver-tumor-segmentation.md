---
title: Deep Learning-Based Liver and Tumor Segmentation
summary: A comparative medical image segmentation study using U-Net, attention variants, and DALU-Net on the 3D-IRCADb CT dataset.
year: 2024
status: completed
researchArea: Medical imaging
methods: [U-Net, Attention U-Net, DALU-Net, data augmentation, CT windowing]
datasets: [3D-IRCADb]
results:
  - The project report records a Dice coefficient of 0.899 for DALU-Net.
  - DALU-Net improved the reported Dice score by 0.077 over the U-Net baseline in the project comparison.
role: Model implementation, data preprocessing, training, evaluation, and comparative analysis within a three-person project team.
collaborators: [Boshen Pan, Shiyang Lin]
featured: true
cover: /assets/projects/liver-segmentation.png
sortOrder: 50
links:
  repository: https://github.com/KunlunLi-Firefly/Liver-Cancer-Segmentation-Using-U-net-and-DALU-Net
---

## Problem

Manual delineation of liver and tumor regions in CT volumes is time-consuming and can vary between readers. This project explored whether progressively richer U-Net variants could improve segmentation quality on a small public medical imaging dataset.

## Approach

The pipeline combined CT windowing, histogram equalization, data augmentation, and supervised segmentation. The comparative study included a baseline U-Net, attention-enhanced variants, deep supervision, and DALU-Net.

## Interpretation

The strongest result in the project report was obtained by DALU-Net. The score is presented as project evidence rather than a clinical performance claim: external validation, uncertainty analysis, and evaluation across institutions would be necessary before drawing broader conclusions.

## What I learned

This work connected data preparation, architecture design, loss selection, training stability, and quantitative evaluation in an end-to-end medical image analysis workflow.
