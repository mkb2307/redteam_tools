import os
import shutil

# Define the paths for vi and nano binaries
vi_path = "/usr/bin/vi"
nano_path = "/usr/bin/nano"

# Temporary paths to hold the binaries during swap
vi_temp = "/usr/bin/vi_temp"
nano_temp = "/usr/bin/nano_temp"

def swap_binaries():
    # Ensure both binaries exist
    if not os.path.exists(vi_path):
        print(f"Error: {vi_path} does not exist.")
        return
    if not os.path.exists(nano_path):
        print(f"Error: {nano_path} does not exist.")
        return

    # Step 1: Move vi to a temporary location
    shutil.move(vi_path, vi_temp)

    # Step 2: Move nano to a temporary location
    shutil.move(nano_path, nano_temp)

    # Step 3: Rename nano_temp to vi and vi_temp to nano
    shutil.move(nano_temp, vi_path)
    shutil.move(vi_temp, nano_path)

    print("Swap complete. 'vi' now opens 'nano' and 'nano' opens 'vi'.")

try:
    swap_binaries()
except PermissionError:
    print("Permission denied. Please run as root.")
except Exception as e:
    print(f"An error occurred: {e}")

