import os 
import shutil

class GetFileinDir():
    
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

    def SaveandRenameOrderBy(self, filenamelist, savepath):
        for item in range(len(filenamelist)):
            name = os.path.join(savepath , str('{:03}'.format(item) + ".bmp"))
            shutil.copy( filenamelist[item],name )



    


