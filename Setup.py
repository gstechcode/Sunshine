import sys
from cx_Freeze import setup, Executable
import os


# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os","tqdm","tkinter","time","zipfile","urllib","shutil","bs4","subprocess","socket"]}
build_dist_options= {"all_users": True, "target_name": "Sunshine_Update.msi"}
# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Sunshine",
    version="1.0",
    description="Sunshine",
    options={
        "build_exe": build_exe_options,
        "bdist_msi": build_dist_options},
    executables=[Executable("UpdateSun.py", base=base, shortcutName= "Sunshine", shortcutDir="DesktopFolder",icon= os.getcwd() + r"\Icon.ico")],
)
