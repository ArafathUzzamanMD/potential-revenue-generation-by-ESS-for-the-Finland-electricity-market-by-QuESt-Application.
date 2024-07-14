# -*- mode: python ; coding: utf-8 -*-
from kivy.tools.packaging.pyinstaller_hooks import get_deps_minimal, get_deps_all, hookspath, runtime_hooks
from kivy_deps import sdl2, glew
import numpy, pandas, scipy, pyomo, matplotlib, seaborn, kivy, xlrd, six, jinja2, bs4, requests, urllib3, holidays, openpyxl, pyutilib, os

numpy_libs = f"{os.path.dirname(numpy.__file__)}.libs"
pandas_libs = f"{os.path.dirname(pandas.__file__)}.libs"
scipy_libs = f"{os.path.dirname(scipy.__file__)}.libs"
matplotlib_libs = f"{os.path.dirname(matplotlib.__file__)}.libs"
pyomo_libs = f"{os.path.dirname(pyomo.__file__)}.libs"
seaborn_libs = f"{os.path.dirname(seaborn.__file__)}.libs"
kivy_libs = f"{os.path.dirname(kivy.__file__)}.libs"
xlrd_libs = f"{os.path.dirname(xlrd.__file__)}.libs"
six_libs = f"{os.path.dirname(six.__file__)}.libs"
jinja2_libs = f"{os.path.dirname(jinja2.__file__)}.libs"
bs4_libs = f"{os.path.dirname(bs4.__file__)}.libs"
requests_libs = f"{os.path.dirname(requests.__file__)}.libs"
urllib3_libs = f"{os.path.dirname(urllib3.__file__)}.libs" 
holidays_libs = f"{os.path.dirname(holidays.__file__)}.libs"
openpyxl_libs = f"{os.path.dirname(openpyxl.__file__)}.libs" 
pyutilib_libs = f"{os.path.dirname(pyutilib.__file__)}.libs"

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['C:\\Users\\duamelo\\.conda\\envs\\valuation_env\\Lib\\site-packages',
            numpy_libs, pandas_libs,
            scipy_libs, matplotlib_libs,
            pyomo_libs, seaborn_libs,
            kivy_libs, xlrd_libs,
            six_libs, jinja2_libs, 
            bs4_libs, requests_libs,
            urllib3_libs, holidays_libs,
            openpyxl_libs, pyutilib_libs
    ],
    hiddenimports=['numpy','pandas','matplotlib',
                    'scipy', 'pyomo', 'seaborn', 
                    'kivy', 'xlrd', 'six', 'jinja2', 
                    'bs4', 'requests', 'urllib3', 
                    'holidays', 'openpyxl', 'pyutilib'],
    datas=[
        ('ci\\*', 'ci'),
        ('data\\*', 'data'),
        ('es_gui\\*', 'es_gui'),
        ('libs\\*', 'libs'),
        ('licenses\\*', 'licenses'),
        ('patch_note_resources\\*', 'patch_note_resources'),
        ('setup.py', '.'),
        ('README.md', '.'),
        ('QuESt.kv', '.'),
        ('main.py', '.'),
        ('LICENSE', '.'),
        ('job.sh', '.'),
        ('.travis.yml', '.'),
        ('.gitignore', '.'),
        ('CHANGELOG.md', '.')
    ],
    hookspath=hookspath(),
    hooksconfig={},
    runtime_hooks=runtime_hooks(),
    noarchive=False,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    optimize=0
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe, Tree('.\\'),
    a.binaries,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
