from PIL import ImageFilter
from PIL import  Image
import os

class Filter():
    def Contour(self,path):
        img = Image.OPEN(path)
        return img.filter(ImageFilter.CONTOUR)

    def Sharpen(self,path):
        img = Image.OPEN(path)
        return img.filter(ImageFilter.SHARPEN)

    def EdgeEnhance(self,path):
        img = Image.OPEN(path)
        return img.filter(ImageFilter.EDGE_ENHANCE)

    def FindEdgeS(self,path):
        img = Image.OPEN(path)
        return img.filter(ImageFilter.FIND_EDGES)

    def ApplyFilter(self,func,dirpath):
        pathlist = os.path.join(dirpath, os.listdir(dirpath))
        imgs = []
        def outputfunc(path):
            return func(path)
        for path in pathlist:
            imgs.append(outputfunc(path))
        return imgs

        
