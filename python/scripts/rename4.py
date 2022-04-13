import os


def myrename(path):
    file_list = os.listdir(path)
    file_list.sort(key=lambda x: int(x[:-4]))  # 倒数第四位'.'为分界线，按照‘.’左边的数字从小到大排序
    i = 0
    for fi in file_list:
        old_name = os.path.join(path, fi)
        new_name = os.path.join(path, str(i)+".png")
        os.rename(old_name, new_name)
        i += 1


if __name__ == '__main__':
    path = r"C:\Users\juliusyang\Desktop\myfile"
    myrename(path)

