import cmd
import os
from imghdr import what
from fileinput import close
from shutil import copyfile
from tokenize import Name
from xml.etree.ElementTree import ProcessingInstruction
while True:
    print(" ")
    ListOfComands = input("write comands: ")
    if ListOfComands == "read":
        ReadFile = input("write name of file: ")
        OpenReadFile = open(ReadFile, "r")
        OpenReadFile.read(ReadFile)
        OpenReadFile.close()
        print(OpenReadFile)
    if ListOfComands == "open":
        OpenFile = input("write name of file: ")
        os.startfile(OpenFile)
    if ListOfComands == "close":
        CloseFile = input("Write name of file: ")
        closeFile = CloseFile.close()
    if ListOfComands == "close.all":
        everythink = "cmd_.py"
        def writeUnder(word):
            import time
            word = word.split()
            for word in word:
                print(word+"\n")
                time.sleep(1)
        writeUnder(". .. ... .... it's_done")
        everythink.close(OpenFile)
        quit()
    if ListOfComands == "rewrite":
        RewriteNameOfFile = input("write name of file: ")
        WhatRewrite = input("write what you want rewrite")
        RewriteNameOfFile = open(RewriteNameOfFile, "w")
        RewriteNameOfFile.write(WhatRewrite)
    if ListOfComands == "write.all":
        DontKnow = input("do you want rewrite file press 1, do you want write in cmd press 2, do you want write in file press 3, or press 4 for stop: ")
        if DontKnow == "1":
           RewriteFile = input("write name of file: ")
           WhatItWant = input("write what od you want rewrite: ")
           RewriteFile = open(RewriteFile, "w")
           RewriteFile.write(WhatItWant)
           RewriteFile.close()
        if DontKnow == "2":
            WriteCmd = input("write what do you want: ")
            print(WriteCmd)
        if DontKnow == "3":
            WriteFile = input("write name of file: ")
            WriteInFile = input("write what do you want write: ")
            writeFile = open(WriteFile, "a")
            writeFile.write( WriteInFile)
            writeFile.close()
        if DontKnow == "4":
            pass
        else:
            print("this comand is invalid")
            close()
    if ListOfComands == "quit":
        quit()
    if ListOfComands == "write":
        Write_File = input("write name of file: ")
        Write_In_File = input("write what do you want write: ")
        Write_File = open(Write_File, "a")
        Write_File.write(Write_In_File)
        Write_File.close(Write_File)
    if ListOfComands == "calculate":
        FirstNumber = float(input("write first number: "))
        Symbol = str(input("write symbol: "))
        SecondNumber = float(input("write second number: "))
        finishNumber = 0
        if Symbol == "/":
            FinishNumber = FirstNumber / SecondNumber
        elif Symbol == "+":
            FinishNumber = FirstNumber + SecondNumber
        elif Symbol == "-":
            FinishNumber = FirstNumber - SecondNumber
        elif Symbol == "*":
            FinishNumber = FirstNumber * SecondNumber
        elif Symbol == "**":
            FinishNumber = FirstNumber ** SecondNumber
        else:
            input("error")
            close()
        def writeUnder(word):
         import time
         word = word.split()
         for word in word:
              print(word)
              time.sleep(0.25)
        print("procesing")
        print(" ")
        writeUnder(" ⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷ ⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷ ⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷")
        print("it's done")
        print(FinishNumber)
    if ListOfComands == "write.cmd":
        writeCmd = input("write what do you want write: ")
        print(writeCmd)
    if ListOfComands == "date":
        import time
        local = time.localtime()
        print("Now is {}. {}. {}".format(local[2], local[1], local[0]))
    if ListOfComands == "note":
        Idk = input("write how the note names: ")
        WhatDoItWan = input("what do you want write: ")
        whatDoItWan = open(Idk, "w")
        whatDoItWan.write(WhatDoItWan)
        whatDoItWan.close()
    if ListOfComands == "del":
        import os
        removeFile = input("write name of file with ADDRESS: ")
        try:
            os.remove(removeFile)
        except FileNotFoundError:
            print("File is not found")
        except PermissionError:
            print("I don't have permission")
        else:
            print("error")
    if ListOfComands == "cl.file":
        nameOfFileForClear = input("write name of file: ")
        NameOfFileForClear = open(nameOfFileForClear, "w")
        NameOfFileForClear.write(" ")
        NameOfFileForClear.close()
    if ListOfComands == "cl.cmd":
        cls = lambda: os.system('cls')
        cls()
    if ListOfComands == "help":
        print("close.all-close all with cmd")
        print("write-write in file")
        print("rewrite-rewrite all in file to you're text")
        print("close-close file")
        print("write.all-show all about writin with rewriting")
        print("open-open file")
        print("quit-quit from cmd")
        print("write.cmd-write you're text in cmd")
        print("read-read a file and write in the cmd")
        print("calculate-calculate any think")
        print("date-show actuali date")
        print("del-delete file")
        print("note-make you're note")
        print("cl.file-clear all in file")
        print("cl.cmd-clear all text in cmd")
