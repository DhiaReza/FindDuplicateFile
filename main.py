# a script to find duplicate files either by name or checksum in a folder
# the checksum algorithm is Adler-32
# the flow :
# 1. choose directory
# 2. list all the files in the choosen directory
# 3. checksum every file in the choosen directory 
# 4. store the checksum value in a list
# 5. check the list for possible duplicate
# 6. delete the duplicate data
# 7. finish 

from functions import *
import os

use_dir = ""

while True:
    print("Directory Mode : \n1. Current Directory\n2. Custom Directory\n3. Exit")
    mode = input("Your Input : ")
    if mode == "1":
        use_dir = current_dir()
    elif mode == "2":
        use_dir = custom_dir()
    elif mode == "3":
        countdown(6)
        break
    else:
        print("Wrong Input")