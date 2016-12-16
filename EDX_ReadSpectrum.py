"""
    Import all *.spc files inside a directory and save as a single *.csv file
"""

# Modules
import struct
import numpy as np
import tkinter as tk
from tkinter import filedialog
from os import listdir

root = tk.Tk()
directory = filedialog.askdirectory(title="Select the folder containing the spectra:", mustexist=True)
root.destroy()

filelist = listdir(directory)
output = np.arange(1,2087,dtype="uint32")

print("----- start -----")
for file in filelist:
    if file.endswith(".spc"):
        with open(directory+"\\"+file, "rb") as f:
            data = np.zeros([2086],dtype="uint32")
            i = 0
        
            f.seek(3848)
            byte = f.read(4)    
            while byte and i<2086:
                data[i] = struct.unpack('I', byte)[0]
                byte = f.read(4)
                i = i + 1
            output = np.column_stack((output, data))

output = np.delete(output, (0), axis=1)
output = np.transpose(output)


np.savetxt(directory+"\\output.csv", output, fmt="%1.1d", delimiter=";")
    
print("===== finished =====")
