#!/usr/bin/env python
#Author : Cipher007

# To-do : 
# - Put output to a file and cat it!
# - Add in date range

import havocui
import havoc
import os, re

sauron_eye = havocui.Widget("SauronEye", True)

demons = []
select_demon = None
dir_to_search = "C:\\Users\\"
filetypes = ".txt"
check_contents = False
check_macros = False
check_filesystem = False
keywords = "pass*"
keywords_dict = "pass*"
extensions_dict = ".txt"


def add_extensions(text):
    global filetypes
    global extensions_dict

    extensions_dict = text
    filetypes = replace(extensions_dict)


def set_directory(text):
    global dir_to_search
    dir_to_search = text

def get_demon(num):
    global demons
    global select_demon
    if num != 0:
        select_demon = havoc.Demon(demons[num-1])

def func_check_contents():
    global check_contents
    check_contents = not check_contents

def func_check_filesystem():
    global check_filesystem
    check_filesystem = not check_filesystem

def func_check_macros():
    global check_macros
    check_macros = not check_macros

def add_keywords(text):
    global keywords
    global keywords_dict

    keywords_dict = text
    keywords = replace(keywords_dict) 

def replace(text):
    pattern = r"\s+"
    return re.sub(pattern, " ", text).strip()

def run_sauron():
    global select_demon
    global filetypes
    global keywords
    global check_contents
    global dir_to_search
    global check_macros
    global check_filesystem

    contents = ""
    #cwd = os.getcwd()
    cwd = "/home/cipher/Github/havoc-SauronEye"
    if select_demon is None:
        havocui.messagebox("ERROR", "Please select a demon!")
        return

    if check_contents:
        contents = "--contents"

    if check_macros:
        macros = "--vbamacrocheck"

    if check_filesystem:
        filesystem = "--systemdirs"

    TaskID = select_demon.ConsoleWrite( select_demon.CONSOLE_TASK, "Tasked demon to run SauronEye!" )

    query = f"-d {dir_to_search} --filetypes {filetypes} {contents} {macros} {filesystem} --keywords {keywords}"
    select_demon.Command(TaskID, "dotnet inline-execute %s/SauronEye.exe %s" % (cwd,query))
    #select_demon.DotnetInlineExecute(TaskID, "%s/SauronEye.exe" % cwd, "%s" % query)

def sauroneye():
    sauron_eye.clear()
    global demons
    demons = havoc.GetDemons()
    sauron_eye.addLabel("<h3 style='color:#bd93f9'>Select a demon to run SauronEye</h3>")
    sauron_eye.addCombobox(get_demon, "Select demon", *demons)
    sauron_eye.addLabel("<span style='color:#71e0cb'>Folder to start search:</span>")
    sauron_eye.addLineedit(dir_to_search, set_directory)
    sauron_eye.addCheckbox("Search file contents", func_check_contents)
    sauron_eye.addCheckbox("Check for macros in .doc and .xls files", func_check_macros)
    sauron_eye.addCheckbox("Search in \%APPDATA% and \%WINDOWS%", func_check_filesystem)
    sauron_eye.addLabel("<span style='color:#71e0cb'>File types seperated by a space:</span>")
    sauron_eye.addLineedit(extensions_dict, add_extensions)
    sauron_eye.addLabel("<span style='color:#71e0cb'>Add keywords to search for seperated by a space:</span>")
    sauron_eye.addLineedit(keywords_dict, add_keywords)

    sauron_eye.addButton("Start", run_sauron)
    sauron_eye.setSmallTab()

sauroneye()
