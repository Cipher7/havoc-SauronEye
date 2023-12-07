#!/usr/bin/env python
#Author : Cipher007

import havocui
import havoc
import os

sauron_eye = havocui.Widget("SauronEye", True)

demons = []
select_demon = None
dir_to_search = "C:\\"
filetypes = ""
check_contents = False
keywords = ""
keywords_dict = ".txt"

# Files to search for
txt_files = False
xml_files = False

def select_text():
    global txt_files
    txt_files = not txt_files

def select_xml():
    global xml_files
    xml_files = not xml_files

def set_directory(text):
    global dir_to_search
    dir_to_search = text

def get_demon(num):
    global demons
    if num != 0:
        select_demon = havoc.Demon(demons[num-1])

def func_check_contents():
    global check_contents
    check_contents = not check_contents

def add_keywords():
    global keywords

def run_sauron():
    global select_demon
    global filetypes
    global keywords
    global txt_files
    global xml_files
    global check_contents
    global dir_to_search

    cwd = os.getcwd()
    if select_demon is None:
        havocui.messagebox("ERROR", "Please select a demon!")

    if txt_files:
        filetypes += " .txt"
    if xml_files:
        filetypes += " .xml"
    if check_contents:
        contents = "--contents"

    TaskID = select_demon.ConsoleWrite( select_demon.CONSOLE_TASK, "Tasked demon to run SauronEye!" )

    query = "-d {dir_to_search} --filetypes{filetypes} {contents} --keywords{keywords}"
 #   select_demon.Command(TaskID, "dotnet inline-execute {cwd}/SauronEye.exe %s" % query)
    print("dotnet inline-execute {cwd}/SauronEye.exe %s" % query)


def sauroneye():
    sauron_eye.clear()
    global demons
    demons = havoc.GetDemons()
    sauron_eye.addLabel("<h3 style='color:#bd93f9'>Select a demon to run SauronEye</h3>")
    sauron_eye.addCombobox(get_demon, "Select demon", *demons)
    sauron_eye.addLabel("<span style='color:#71e0cb'>Folder to start search:</span>")
    sauron_eye.addLineedit(dir_to_search, set_directory)
    sauron_eye.addCheckbox("Search file contents", func_check_contents)
    sauron_eye.addLabel("<span style='color:#71e0cb'>File types:</span>")
    sauron_eye.addCheckbox("Text files (*.txt)", select_text)
    sauron_eye.addCheckbox("XML files (*.xml)", select_xml)
    sauron_eye.addLabel("<span style='color:#71e0cb'>Add keywords to search for seperated by a comma:</span>")
    sauron_eye.addLineedit(keywords_dict, add_keywords)

    sauron_eye.addButton("Start", run_sauron)
    sauron_eye.setSmallTab()

sauroneye()
