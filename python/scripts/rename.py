import os
def myrename(path):
    file_list=os.listdir(path)
    i=0



    for fi in file_list:
        old_name=os.path.join(path,fi)
        new_name=os.path.join(path,str(i)) + ".png"
        os.rename(old_name,new_name)
        i+=1
        
# //之后调用这个函数，传入path即可

if __name__=="__main__":
    #  for i in range(4658):
         path = r"C:\Users\juliusyang\Desktop\myfile" #+ str(i) + "/"
         myrename(path)
# # //这里以10个目录为例