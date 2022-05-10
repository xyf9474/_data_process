import os
import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pylab as plt
import nibabel as nib
from nibabel import nifti1
from nibabel.viewers import OrthoSlicer3D
import numpy as np
from tqdm import tqdm

root_path = r'F:\mismatch'
namedir = os.listdir(root_path)
list = []
num = 0
for name in tqdm(namedir):
    isName = 0
    num += 1
    name_path = os.path.join(root_path,name)
    cc_img = None
    roi_img = None
    for item in os.listdir(name_path):
        if item == 'CrackedCapsule.nii.gz':
            # 先用nib.load读取nii图像，再用asarray转换为np.array格式
            cc_img = np.asarray(nib.load(os.path.join(name_path,item)).get_fdata())
        if item == 'roi.nii.gz':
            roi_img = np.asarray(nib.load(os.path.join(name_path,item)).get_fdata())
    for i in range(cc_img.shape[0]):
        if isName == 1:
            break
        for j in range(cc_img.shape[1]):
            if isName == 1:
                break
            for k in range(cc_img.shape[2]):
                if cc_img[i][j][k] == 1 and roi_img[i][j][k] == 1 :
                    isName = 1
                    break

    if isName == 0:
        list.append(name)
print(list)