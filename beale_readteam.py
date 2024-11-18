import os
import shutil

# Define the paths for vi and nano binaries
vi_path = "/usr/bin/vi"
nano_path = "/usr/bin/nano"

# Temporary paths to hold the binaries during swap
vi_temp = "/usr/bin/vi_temp"
nano_temp = "/usr/bin/nano_temp"

def swap_binaries():
    shutil.move(vi_path, vi_temp)
    shutil.move(nano_path, nano_temp)
    shutil.move(nano_temp, vi_path)
    shutil.move(vi_temp, nano_path)
