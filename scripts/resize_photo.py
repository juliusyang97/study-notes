# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 16:06:35 2018
@author: libo
"""
from PIL import Image
import os
 
 
def image_resize(image_path, new_path):           # 统一图片尺寸
    print('============>>修改图片尺寸')
    for img_name in os.listdir(image_path):
        img_path = image_path + "/" + img_name    # 获取该图片全称
        image = Image.open(img_path)              # 打开特定一张图片
        image = image.resize((640, 640))          # 设置需要转换的图片大小
        # process the 1 channel image
        image.save(new_path + '/'+ img_name)
    print("end the processing!")
 
 
if __name__ == '__main__':
    print("ready for ::::::::  ")
    ori_path = r"F:\a_research\Research_data\test"                # 输入图片的文件夹路径
    new_path = r'F:\a_research\Research_data\test\resize'                   # resize之后的文件夹路径
    image_resize(ori_path, new_path)
