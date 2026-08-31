---
title: Skin Lesion Segmentation and Classification
summary: A course project exploring classical segmentation, symmetry features, and machine-learning classification for dermoscopic skin lesion images.
year: 2024
status: coursework
researchArea: Medical imaging
methods: [Otsu thresholding, mathematical morphology, symmetry analysis, Random Forest, cross-validation]
datasets: [150 dermoscopic images across three lesion classes]
results:
  - Established an evaluation plan using IoU for segmentation and F1 score for classification.
  - The available report describes preliminary methods and planned evaluation, so no final performance number is claimed here.
role: Course project contribution to segmentation, feature extraction, and classification planning.
collaborators: []
featured: false
cover: /assets/projects/skin-lesion.png
sortOrder: 20
links:
  repository: https://github.com/KunlunLi-Firefly/Skin_Lesion
---

## Problem

Skin lesion analysis involves both locating the lesion and distinguishing clinically relevant visual patterns. The small, imbalanced dataset in this project makes careful evaluation especially important.

## Approach

The proposed pipeline converted images to grayscale, applied Otsu thresholding and morphology, derived lesion shape and symmetry features, and planned a Random Forest classifier with cross-validation.

## Evidence boundary

The source report explicitly describes the methods as under evaluation. The project page therefore avoids the stronger completion and accuracy claims that appeared in the legacy website.
