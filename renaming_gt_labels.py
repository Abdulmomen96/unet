import numpy as np

import os
from glob import glob
set_0 = r'C:\Users\USER\Documents\MATLAB\set0'

#labels = glob(r'D:\data2\csa\label\\*')
images = glob(r'D:\data2\csa\test\\*')
#labels_dir = r'D:\data2\csa\label\\'
images_dir = r'D:\data2\csa\test\\'

print(len(images))

def givenumbers(s):
    test = os.path.split(s)[1]
    test = test.replace('_', '.')
    return int(test.split('.')[1])



#labels = sorted(labels)#,key=lambda x: givenumbers(x))
images = sorted(images)#,key=lambda x: givenumbers(x))
import shutil

i = 0
for image in images: #label, image in zip(labels, images):
    image_name = str(i) + '.png' #image.replace('.', '\\').split('\\')[-2] + '.png'
    #print(label, labels_dir + image_name)
    print(image, images_dir + image_name)
    #shutil.move(label, labels_dir + image_name)
    shutil.move(image, images_dir + image_name)
    i += 1

    print(image_name)
    print()

