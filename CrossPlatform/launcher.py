import os
import sys
import subprocess

# Determine the directory where this script is located
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

# Go up one level to the 'CrossPlatform' folder
crossplatform_directory = os.path.dirname(script_directory)

# Define the path to the 'update_flac_metadata.py' script
update_flac_metadata_path = os.path.join(crossplatform_directory, 'Python Scripts', 'update_flac_metadata.py')

# Replace the path below with the full path to the desired Python interpreter on your system
python_path = "C:\\Users\\B\\AppData\\Local\\Programs\\Python\\Python39\\python.exe"

# Run the 'update_flac_metadata.py' script using a new command prompt that stays open
# subprocess.call(f'cmd.exe /k "{python_path} \"{update_flac_metadata_path}\""')

# Run the 'update_flac_metadata.py' script without opening a new command prompt
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

subprocess.Popen([python_path, update_flac_metadata_path], startupinfo=startupinfo)

