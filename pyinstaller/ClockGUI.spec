# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['clock_gui.py'],
             pathex=['/Documents/clockGUI'],
             binaries=[],
             datas=[],
             hiddenimports=['tkinter', 'packaging.requirements', 'packaging.specifiers', 'packaging.version', 'pkg_resources.markers'],
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
          name='ClockGUI',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='clockicon.icns')
app = BUNDLE(exe,
             name='ClockGUI.app',
             icon='clockicon.icns',
             bundle_identifier=None)
