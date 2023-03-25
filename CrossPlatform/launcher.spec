# launcher.spec

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Add this line to include the "Python Scripts" folder
added_files = [('Python Scripts/', 'Python Scripts')]

a = Analysis(['launcher.py'],
             pathex=['/Users/benharding/Library/Application Support/REAPER/Scripts/SoundDesignSpottingListSystem/CrossPlatform'],
             binaries=[],
             datas=[('/Users/benharding/Library/Application Support/REAPER/Scripts/SoundDesignSpottingListSystem/CrossPlatform/my_macos_virtual_environment/lib/python3.11/site-packages/mutagen', 'mutagen')] + added_files,
             hiddenimports=[],
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
          a.binaries + [('libpython3.11.dylib', '/Users/benharding/Library/Application Support/REAPER/Scripts/SoundDesignSpottingListSystem/CrossPlatform/my_macos_virtual_environment/lib/python3.11/lib-dynload/libpython3.11.dylib', 'BINARY')],
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

