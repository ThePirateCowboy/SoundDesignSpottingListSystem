# launcher_windows.spec
import sys
from PyInstaller.utils.hooks import collect_data_files, collect_submodules
sys.modules['FixTk'] = None

block_cipher = None

added_files = [('Python Scripts', 'Python Scripts')]

# Collect data files and submodules from 'mutagen' package
mutagen_data = collect_data_files('mutagen')
mutagen_submodules = collect_submodules('mutagen')

a = Analysis(['launcher.py'],
             pathex=['C:\\Users\\B\\AppData\\Roaming\\REAPER\\Scripts\\SoundDesignSpottingListSystem\\CrossPlatform'],
             binaries=[],
             datas=mutagen_data + added_files,
             hiddenimports=['mutagen'] + mutagen_submodules,  # Add 'mutagen' as a hidden import
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
             
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='launcher',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
