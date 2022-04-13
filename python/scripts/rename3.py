import os

folder_path = r'C:\Users\juliusyang\Desktop\myfile'
num = 0

if __name__ == '__main__':
    for file in os.listdir(folder_path):
        s = '%06d' % num  # 前面补零占位
        os.rename(os.path.join(folder_path, file), os.path.join(folder_path,  str(s) + '.png'))
        num += 1
