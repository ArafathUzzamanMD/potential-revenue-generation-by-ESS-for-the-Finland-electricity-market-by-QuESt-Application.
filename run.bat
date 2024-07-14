@echo off
set PYTHON_URL=https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe
set GLPK_URL=https://deac-fra.dl.sourceforge.net/project/winglpk/winglpk/GLPK-4.65/winglpk-4.65.zip?viasf=1


::change directory to C:\Users\%USERNAME%\Desktop\Valuation FI
cd "C:\Users\%USERNAME%\Desktop\Valuation FI\"


:: Download Python installer if not already downloaded
if not exist python-installer.exe (
    powershell -Command "& { iwr '%PYTHON_URL%' -OutFile python-installer.exe }"
) else (
    echo Python installer already downloaded
)


:: Install Python if not already installed
if not exist "C:\Program Files\Python38\python.exe" (
    python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
) else (
    echo Python is already installed
)


:: Check Python installation status
if ERRORLEVEL 1 (
    echo Python installation failed!
    exit /b %ERRORLEVEL%
) else (
    echo Python installation succeeded!
)


:: Add Python to PATH
setx PATH "%PATH%;C:\Program Files\Python38"


:: Create and activate virtual environment
if not exist test_env (
    "C:\Program Files\Python38\python.exe" -m venv test_env
)
call test_env\Scripts\activate




:: if not exists setuptools, install setuptools and other required packages
@REM if not exist  C:\users\%USERNAME%\appdata\roaming\python\python38\site-packages (
:: install setuptools
"C:\Program Files\Python38\python.exe" -m pip install --upgrade pip setuptools


"C:\Program Files\Python312\python.exe" -m pip install -U git+https://github.com/PyUtilib/pyutilib.git


"C:\Program Files\Python38\python.exe" -m pip install pyomo==6.5


"C:\Program Files\Python38\python.exe" -m pip install -U kivy


"C:\Program Files\Python38\python.exe" -m pip install kivy_deps.glew kivy_deps.sdl2 kivy_deps.gstreamer kivy kivy_examples --pre


:: Install required packages from setup.py
"C:\Program Files\Python38\python.exe" -m pip install . --no-warn-script-location


@REM ) else (
@REM     echo setuptools and other packages already installed
@REM )




:: Add glpk-4.65/w64 to PATH
@REM copy .\glpk-4.65\ C:\glpk-4.65
set PATH=%PATH%;C:\Users\%USERNAME%\Desktop\Valuation FI\glpk-4.65\w64




:: Run main.py
"C:\Program Files\Python38\python.exe" main.py