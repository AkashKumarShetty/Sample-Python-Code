import os
import re

def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir(r"C:\Users\akash\Downloads\prank")

    # print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir(r"C:\Users\akash\Downloads\prank")

    # (2) for each file, rename file name
    for file_name in file_list:
        print("Old Name - " + file_name)
        #print("New Name - " + file_name.translate("0123456789"))
        new_name = re.sub('[0-9]', '', file_name)
        print(new_name)
        os.rename(file_name, new_name)
    os.chdir(saved_path)

rename_files()
