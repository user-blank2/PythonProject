import os

file_name="hello.txt"

if os.path.exists(file_name):
    print("That file exist")