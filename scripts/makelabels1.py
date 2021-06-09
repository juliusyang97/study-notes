import os
import os.path

path = "../yolov5/data/all_data/images/"


for filenames in os.walk(path):
    filenames = list(filenames)
    filenames = filenames[2]
    for filename in filenames:
        print(filename)
        with open ("../yolov5/data/all_data/train1.txt",'a') as f:
            f.write(path+filename+'\n')


