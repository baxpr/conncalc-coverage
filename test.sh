#!/usr/bin/env bash

./compute_coverage.py \
    --meanfmri INPUTS/wmeanadfmri.nii.gz \
    --roi_niigz INPUTS/rroi.nii.gz \
    --roilabels_csv INPUTS/rroi-labels.csv \
    --out_dir OUTPUTS
