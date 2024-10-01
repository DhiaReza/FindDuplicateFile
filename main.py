# a script to find duplicate files either by name or checksum in a folder
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