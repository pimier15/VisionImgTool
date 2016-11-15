import ColorConvert

clc = ColorConvert.ColorConvertor()

PassInput0 = r"D:\002ImageClassificationData\01_ SamTransistor\First\Pass\Gray"
PassInput1 = r"D:\002ImageClassificationData\01_ SamTransistor\Second\Gray\Pass"
FailInput0 = r"D:\002ImageClassificationData\01_ SamTransistor\First\Fail\Gray"
FailInput1 = r"D:\002ImageClassificationData\01_ SamTransistor\Second\Gray\Fail"

PassOutpath = r"D:\002ImageClassificationData\01_ SamTransistor\ALl\Gray\Pass"
FailOutpath = r"D:\002ImageClassificationData\01_ SamTransistor\ALl\Gray\Fail"



PassInput0List = []
PassInput1List = []
PassList = []

PassInput0List = clc.GetPathFilesinRootFolder(PassInput0)
PassInput1List = clc.GetPathFilesinFolder(PassInput1)
PassList = PassInput0List + PassInput1List
clc.ToGray( PassList , PassOutpath)


FailInput0List = []
FailInput1List = []
FailList = []

FailInput0List = clc.GetPathFilesinRootFolder(FailInput0)
FailInput1List = clc.GetPathFilesinFolder(FailInput1)
FailList = FailInput0List + FailInput1List
clc.ToGray( FailList , FailOutpath)

