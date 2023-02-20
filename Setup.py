import sys
from cx_Freeze import setup, Executable
import os


# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os","unidecode","pyautogui","datetime","zipfile","PyQt5","json","tkinter","shutil","reportlab","PIL","subprocess","psutil","imageio","cv2"], "include_files" : [
    ("./Cache","./Cache"),
    ("./Images","./Images"),
    ("./Tools","./Tools"),
    ("./Fonts","./Fonts"),
    ("./Models","./Models"),
    (".version",".version"),
    (".multimeshscripting","./multimeshscripting"),
    ], "include_msvcr": True}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Sunshine",
    version="1.0",
    description="Sunshine",
    options={"build_exe": build_exe_options},
    executables=[Executable("Sunshine.py", base=base, icon= os.getcwd() + r"\Images\Icon.ico")],
)
