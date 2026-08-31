---
title: SSLAL for Depth-Enhanced Sign Language Recognition
summary: A data-efficient isolated sign recognition pipeline combining monocular depth refinement, semi-supervised learning, and active learning.
year: 2024
status: manuscript
researchArea: Data-efficient vision
methods: [Depth Anything V2, MediaPipe, Transformer, semi-supervised learning, active learning, uncertainty sampling]
datasets: [ASL-CITIZEN, MS-ASL, WLASL, GISLR]
results:
  - The manuscript reports lower word error rate for SSLAL than the corresponding baseline across evaluated datasets.
  - The depth-enhanced SSLAL table reports F1 values up to 0.992 on WLASL and 0.988 on MS-ASL.
  - Results are stated by dataset and metric rather than summarized as a single unsupported accuracy value.
role: Co-author; contributed to depth-enhanced landmark representation and the active and semi-supervised learning pipeline.
collaborators: [Runzhou Chen, Yixuan Wang, Eric Nalisnick]
featured: true
cover: /assets/projects/sign-language-depth.png
sortOrder: 60
links:
  repository: https://github.com/KunlunLi-Firefly/Sign_Language
---

## Problem

Sign language recognition systems face limited labeled data, variable video quality, occlusions, and incomplete depth information. These constraints make both representation quality and annotation efficiency central challenges.

## Approach

The pipeline combines 2D landmarks from MediaPipe with monocular depth estimates from Depth Anything V2. A refinement stage addresses overlapping and missing landmarks before a Transformer-based recognizer is trained using pseudo-labeling, consistency regularization, and active sample selection.

## Evaluation

The manuscript reports dataset-specific word error rate and F1 results for baseline, SSLAL, depth-enhanced baseline, and depth-enhanced SSLAL conditions. Keeping those dimensions visible makes the evidence more useful than a single aggregate percentage.

## Status

This item is presented as a research manuscript. A publication venue has not been asserted because it was not verified from the available public sources.
