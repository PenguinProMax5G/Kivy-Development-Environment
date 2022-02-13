# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew
from kivymd import hooks_path as kivymd_hooks_path



block_cipher = None


a = Analysis([r'C:\Users\samad\OneDrive\Projects\kivy-development-environment\tools\kivy-development-environment\widget\main.py'],
             pathex=[],
             binaries=[],
             datas=[(r'C:\Users\samad\OneDrive\Projects\kivy-development-environment\tools\kivy-development-environment\widget\scripts', 'scripts/'), (r'C:\Users\samad\OneDrive\Projects\kivy-development-environment\tools\kivy-development-environment\widget\kv-files', 'kv-files/'), (r'C:\Users\samad\OneDrive\Projects\kivy-development-environment\venv\Lib\site-packages\plyer', 'plyer/')],
             hiddenimports=[],
             hookspath=[kivymd_hooks_path],
             hooksconfig={},
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
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
