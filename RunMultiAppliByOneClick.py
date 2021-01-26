import os
import json
import tkinter as tk
from tkinter import filedialog

print("RunMultiAppliByOneClick")
# User input 
filename = input('Enter the name of the file to be created: ')

# JSON file to hold the paths of executables
paths = {}
paths['path'] = []

# Open File Dialog to choose one by one executable file 
root = tk.Tk()
root.withdraw()
while (True):
    file_path = filedialog.askopenfilename(  title='Select executable file...', filetypes=( ("Executable", "*.exe"), )  )
    if (file_path == ""):
        break
    else:
        paths['path'].append({ 'url': file_path })

# load json file
with open('paths.txt', 'w') as outfile:
    json.dump(paths, outfile)

# create batch-file
newBat = open(r''+ filename + '.bat','w+')
newBat.write('@echo off\n')

# write the start commands in the batch-file
with open('paths.txt') as json_file:
    data = json.load(json_file)
    for p in data['path']:
        newBat.write( 'start "" "' + p['url'] + '"\n')
newBat.close()