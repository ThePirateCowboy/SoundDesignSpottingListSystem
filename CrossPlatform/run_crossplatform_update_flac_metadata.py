import os
import sys
import subprocess

def run_windows_commands(venv_path, script_path):
    activate_script = os.path.join(venv_path, 'Scripts', 'activate.bat')
    command = f'call "{activate_script}" && python "{script_path}"'
    subprocess.run(command, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)

def run_unix_commands(venv_path, script_path):
    activate_script = os.path.join(venv_path, 'bin', 'activate')
    command = f'source "{activate_script}" && python3 "{script_path}"'
    subprocess.run(['bash', '-c', command])

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Script dir: {script_dir}")

    if sys.platform == 'win32':
        venv_path = os.path.join(script_dir, 'my_windows_virtual_environment_crossplatform')
    elif sys.platform in ('linux', 'linux2', 'darwin'):
        venv_path = os.path.join(script_dir, 'my_macos_virtual_environment')
    else:
        print(f'Unsupported platform: {sys.platform}')
        return

    print(f"Virtual env path: {venv_path}")
    script_path = os.path.join(script_dir, 'Python Scripts', 'update_flac_metadata.py')
    print(f"Script path: {script_path}")

    if sys.platform == 'win32':
        run_windows_commands(venv_path, script_path)
    elif sys.platform in ('linux', 'linux2', 'darwin'):
        run_unix_commands(venv_path, script_path)


if __name__ == '__main__':
    main()
