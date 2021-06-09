
import os
from os import listdir, getcwd
from os.path import join

if __name__ == '__main__':
    source_folder =r'/home/user/yjq/yolov5/data/all_data/images'
    dest = r'/home/user/yjq/yolov5/data/all_data/train.txt'
    dest2 = r'/home/user/yjq/yolov5/data/all_data/val.txt'
    file_list = os.listdir(source_folder)
    train_file = open(dest, 'a')
    val_file = open(dest2, 'a')
    i=0
    for file_obj in file_list:
        file_name, file_extend = os.path.splitext(file_obj)

        if (i%4 ==0):
           #val_file.write(file_name+".jpg" + '\n')  
            val_file.write("/home/user/yjq/yolov5/data/all_data/images/"+file_name+".jpg" + '\n')
        else:
           #train_file.write(file_name+".jpg" + '\n')
           train_file.write("/home/user/yjq/yolov5/data/all_data/images/"+file_name+".jpg" + '\n')
        i+=1
    train_file.close()
val_file.close()
