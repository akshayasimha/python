import os

dir_name = input("Enter the directory name to be created: ")
dir_name = dir_name.lower()
if dir_name == "con" or dir_name == "lpt" or dir_name == "prn" or dir_name == "aux":
    print(
        "These names are reserved for Windows operating systems.\nYou cannot create the directory named %s." % dir_name)
elif os.path.exists(dir_name):
    print("The directory path already exists. Try another name.")
else:
    print("Success - Directory is created.")
    os.mkdir(dir_name)
