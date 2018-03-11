# -*- mode: python -*-

block_cipher = None


a = Analysis(['AutoComment.py'],
             pathex=['D:\\Documents\\AutoComment'],
             binaries=[],
             datas=[('img/0.jpg', './img'),('img/1.jpg', './img'),('img/2.jpg', './img'),('img/3.jpg', './img'),('img/4.jpg', './img'),('windows.exe', '.'),('linux', '.'),('mac', '.'),('joke.txt', '.'),('url.txt', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='AutoComment',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='AutoComment')
