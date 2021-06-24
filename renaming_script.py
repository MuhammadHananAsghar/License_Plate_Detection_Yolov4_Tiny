import os

PATH = "/home/zerosec/Downloads/Model_Files/yolov3/dataset/images"

for index, oldfile in enumerate(os.listdir(PATH), start=1):
    oldfile = PATH+'/'+oldfile    
    newfile = PATH+'/'+'{}.jpg'.format(index)
    os.rename(oldfile,newfile)
