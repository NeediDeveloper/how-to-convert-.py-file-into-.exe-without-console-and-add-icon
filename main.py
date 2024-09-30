# TODO First Step
# First Install The Module
# pip install pyinstaller

# TODO Second Step
# Open The Folder Where Is Your File And Type cmd in The Top Bar

# TODO Third Step
# Type the following line:
# pyinstaller --onefile Your_File_Name.py

# TODO Fourth Step 
# pyinstaller --onefile --windowed Your_File_Name.py
# You Got a amazing error
# use the following line of code in you .py file
import sys
import os
if getattr(sys, 'frozen', False):
    sys.stdout = open(os.devnull, 'w')
    sys.stderr = open("error.log", 'w')


# TODO Fifth Step
# pyinstaller --onefile --windowed --icon=icon.ico Your_File_Name.py

# TODO Last Step
# Copmressed to a zip file
