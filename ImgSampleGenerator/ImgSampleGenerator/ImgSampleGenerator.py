import keras
import numpy as np
import os
from keras.preprocessing.image import ImageDataGenerator , array_to_img, img_to_array, load_img

from Tkinter import Tk
from tkFileDialog import askdirectory

import GetFilePathFromDir as getfdir



Tk().withdraw()
PathMana = getfdir.GetFileinDir()
datagen = ImageDataGenerator(
    rotation_range=0.1,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True,
    vertical_flip=True,
    dim_ordering='th',
    fill_mode='nearest'
    )

dirpath = askdirectory()
outputdirpath = askdirectory()
FilenameList = PathMana.GetPathFilesinFolder(dirpath)

#outputdirpath = "D:\A_002ImageClassificationData\kerasSample"

arrimglist = []


namenum = 0
for imgpath in  FilenameList:
    img = load_img(imgpath)
    arrimg = img_to_array(img)
    arrimg = np.reshape(arrimg,(1,)+arrimg.shape)
    count = 0
    tempname = format(namenum, "03d") 
    for item in datagen.flow(arrimg, batch_size=1, save_to_dir = outputdirpath,save_prefix=tempname,save_format='bmp'):
        count += 1
        namenum += 1;
        if count == 10:
          break;


