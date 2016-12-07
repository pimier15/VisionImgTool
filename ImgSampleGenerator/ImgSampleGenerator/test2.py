import cv2

path = r"D:\A_002ImageClassificationData\01_ SamTransistor\failoutput\000_0_2838.bmp"
outpath =r"D:\A_002ImageClassificationData\01_ SamTransistor\Temp\000_0_2838.bmp"

img = cv2.imread(path,0)
resized = cv2.resize(img,(124,124),cv2.INTER_NEAREST)
cv2.imwrite(outpath,resized)
