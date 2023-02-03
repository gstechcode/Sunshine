import sys
from cx_Freeze import setup, Executable
import os


# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os","unidecode","pyautogui","datetime","zipfile","PyQt5","json","tkinter","shutil","reportlab","PIL","subprocess","psutil"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="PyRelator",
    version="1.0",
    description="PyRelator",
    options={"build_exe": build_exe_options},
    executables=[Executable("PyRelator.py", base=base, icon= os.getcwd() + r"\Images\Icon.ico")],
)
