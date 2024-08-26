#!/usr/bin/env python

import argparse
import nibabel
import nilearn
from nilearn import masking, maskers
import numpy
import os
import pandas

parser = argparse.ArgumentParser()
parser.add_argument('--meanfmri_niigz', required=True)
parser.add_argument('--roi_niigz', required=True)
parser.add_argument('--roilabels_csv', required=True)
parser.add_argument('--out_dir', required=True)
args = parser.parse_args()

# Threshold mean fmri using Nichols antimode method
img = nibabel.load(args.meanfmri_niigz)
img_mask = nilearn.masking.compute_epi_mask(img)
nibabel.save(img_mask, os.path.join(args.out_dir, 'mask.nii.gz'))

roi_info = pandas.read_csv(args.roilabels_csv)

masker = nilearn.maskers.NiftiLabelsMasker(args.roi_niigz)

fracs = masker.fit_transform(img_mask)

roi_info['PctCoverage'] = [100*x[0] for x in numpy.transpose(fracs).tolist()]

roi_info.to_csv(os.path.join(args.out_dir, 'coverage.csv'), index=False)

