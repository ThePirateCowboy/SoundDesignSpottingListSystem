# launcher_windows.spec

block_cipher = None

# Add this line to include the "Python Scripts" folder
added_files = [('Python Scripts\\', 'Python Scripts\\')]

a = Analysis(['launcher.py'],
             pathex=['C:\\Users\\B\\AppData\\Roaming\\REAPER\\Scripts\\SoundDesignSpottingListSystem\\CrossPlatform'],
             binaries=[],
             datas=added_files,
             hiddenimports=['mutagen'],
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
          runtime_tmpdir=None,
          console=False )
