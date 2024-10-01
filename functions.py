import os
import time

#use current directory
def current_dir():
    # use current directory
    full_path = os.path.realpath(__file__)
    dir_path = os.path.dirname(full_path)
    global dir
    dir = dir_path
    return dir_path

#use custom directory
def custom_dir():
    # user inputed directory
    dir_path = input("Copy and Paste you directory here : ")
    global dir
    dir = dir_path
    return dir_path

# get list of files
def get_files(dir_path):
    # get file list in a directory
    try:
        files_names = os.listdir(dir_path)
        print("Your Files : ")
        for x in files_names:
            print((files_names.index(x)+1),". ",x)
        print("")
        return files_names
    except:
        print("There are no such directory!")
        print("Your input : ", dir_path)
        return False

#just a countdown
def countdown(t): 
    while t: 
        #mins, secs = divmod(t, 60) 
        #timer = '{:02d}:{:02d}'.format(mins, secs) 
        #print(timer, end="\r")
        t -= 1
        time.sleep(1) 
        print(f'{t}')