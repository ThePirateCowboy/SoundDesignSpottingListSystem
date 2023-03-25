import os
import sys
import subprocess

def run_python_script(script_path):
    if sys.platform == 'win32':
        python_executable = 'python'
    else:
        python_executable = 'python3'

    command = f'{python_executable} "{script_path}"'
    subprocess.run(command, shell=True)

def main():
    # Check if the script is running as a standalone executable
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    script_path = os.path.join(base_path, 'Python Scripts', 'update_flac_metadata.py')

    run_python_script(script_path)

if __name__ == '__main__':
    main()

