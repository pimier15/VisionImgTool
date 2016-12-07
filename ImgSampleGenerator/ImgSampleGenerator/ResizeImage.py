import GetFilePathFromDir as getfdir
import cv2
import os
from Tkinter import Tk
from tkFileDialog import askdirectory

Tk().withdraw()

indirpath  = askdirectory()
outdirpath = askdirectory()

GetPath = getfdir.GetFileinDir()

ImgList = GetPath.GetPathFilesinFolder(indirpath)

count = 0
for imgpath in ImgList:
    tempimg = cv2.imread(imgpath,0)
    resized = cv2.resize(tempimg,(124,124), cv2.INTER_NEAREST)
    name = format(count,"03d") + ".bmp"
    fullname = os.path.join(outdirpath,name,)
    cv2.imwrite(fullname,resized)
    count+=1