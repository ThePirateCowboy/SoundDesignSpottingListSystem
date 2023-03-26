import sys
sys.path.append("c:/users/b/appdata/roaming/reaper/scripts/sounddesignspottinglistsystem/crossplatform/my_windows_virtual_environment_crossplatform/lib/site-packages")

import os
import ctypes
import subprocess

def hide_terminal():
    if sys.stdout is not None and sys.stdout.isatty():
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hwnd:
            ctypes.windll.user32.ShowWindow(hwnd, 0)

def main():
    #hide_terminal()

    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'run_crossplatform_update_flac_metadata.py')
    python_executable = sys.executable

    print(f"Python Executable: {python_executable}")
    print(f"Script Path: {script_path}")

    result = subprocess.call([python_executable, script_path])
    print(f"Script Result: {result}")

if __name__ == "__main__":
    main()
