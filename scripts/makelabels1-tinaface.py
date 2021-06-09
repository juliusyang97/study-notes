import os
#import os.path


path = "/home/user/yjq/vedadet/data/DJI_0009-1/images/"

filenames = os.path.basename(__file__)
print(filenames)

for filenames in os.walk(path):
    #filenames = list(filenames)
    filenames = os.path.basename(__file__)
    filenames = filenames.split('.')[0]
    for filename in filenames:
        print(filename)
        with open ("../vedadet/data/DJI_0009-1/train1.txt",'a') as f:
            f.write(path+filename+'\n')


