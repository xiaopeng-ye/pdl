# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main_gui.pyw'],
             pathex=['C:\\Users\\yezy\\OneDrive\\UPM\\Procesadores de Lenguajes\\practica\\pdl\\src'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas +=[("config/descendente_tabular.csv","C:\\Users\\yezy\\OneDrive\\UPM\\Procesadores de Lenguajes\\practica\\pdl\\src\\config\\descendente_tabular.csv","DATA"),
("config/lexico_tabla.csv","C:\\Users\\yezy\\OneDrive\\UPM\\Procesadores de Lenguajes\\practica\\pdl\\src\\config\\lexico_tabla.csv","DATA"),
("config/producciones.txt","C:\\Users\\yezy\\OneDrive\\UPM\\Procesadores de Lenguajes\\practica\\pdl\\src\\config\\producciones.txt","DATA")
]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main_gui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main_gui')
