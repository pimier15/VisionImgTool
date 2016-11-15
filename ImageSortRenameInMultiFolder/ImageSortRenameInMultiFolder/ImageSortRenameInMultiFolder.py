import ImgSorRename as imgrename
import os

classs = imgrename.ImgSorRename()
inputpath = r"D:\002ImageClassificationData\01_ SamTransistor\First\Pass\Gray"
outputpath = r"D:\002ImageClassificationData\01_ SamTransistor\First\Sort\Gray_PassAll"

filepath = os.listdir(inputpath)

imgspath = classs.GetPathFilesinRootFolder(inputpath)
classs.SaveandRenameOrderBy( imgspath , outputpath)
