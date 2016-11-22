import GetFilePathFromDir as getfdir
import os
from Tkinter import Tk
from tkFileDialog import askdirectory

Tk().withdraw()
inputdirnmae = askdirectory()
outputdirname = askdirectory()

PathMana = getfdir.GetFileinDir()

imgspath = PathMana.GetPathFilesinRootFolder(inputdirnmae)

#classs.SaveandRenameOrderBy( imgspath , outputdirname)
