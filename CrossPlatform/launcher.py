import os
import sys
import platform
from run_crossplatform_update_flac_metadata import main

def hide_terminal():
    if platform.system() == "Windows":
        import ctypes

        hWnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hWnd:
            ctypes.windll.user32.ShowWindow(hWnd, 0)

    elif platform.system() == "Darwin":
        import AppKit

        AppKit.NSApplication.sharedApplication().activateIgnoringOtherApps_(True)
        AppKit.NSApplication.sharedApplication().setActivationPolicy_(1)

if __name__ == "__main__":
    hide_terminal()
    main()

