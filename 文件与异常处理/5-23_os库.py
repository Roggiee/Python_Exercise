import os
path=r"C:\hp"
file_list=os.listdir(path)
for file in file_list:
    print(file)
file_list=os.listdir(".")
for file in file_list:
    print(file)