from PIL import Image
import os

class ColorConvertor():
    def GetPathFilesinFolder(self,dirpath):
        filepath = os.listdir(dirpath)
        output = [ os.path.join(dirpath, item) for item in filepath]
        return output

    def GetPathFilesinRootFolder(self,rootpath):
        folderPath = os.listdir(rootpath)
        subfolderpath = [ os.path.join(rootpath, item) for item in folderPath]
        output = []
        for dirpath in subfolderpath:
            output = output + self.GetPathFilesinFolder(dirpath)
        return output

    def ToGray(self,pathlist,outputpath):
        for i in range(len(pathlist)):
            Image.open(pathlist[i]).convert("L").save( os.path.join(outputpath , str('{:03}'.format(i) + ".bmp")))
