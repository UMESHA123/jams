import cx_Freeze
import sys
import os
base = None
if sys.platform == 'win64':
    base = "Win64GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\acer\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\acer\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

executables = [cx_Freeze.Executable("main_page.py", base=base)]

cx_Freeze.setup(
    name = "Jams",
    options = {"build_exe": {"packages":["tkinter","os","sys"], "include_files":['tcl86t.dll','tk86t.dll']}},
    version = "1.00",
    description = "Jams| Developed by umesha ramesha hugger ",
    executables = executables
    )
