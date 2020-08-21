import os

print("\t\t\t\t\t\t Hello! I here for your assistance. Just type in what I would like to open for you.")
print()
while True:   
    print("\t\t\t\t\t\tWhat Program would you like to open?")
    p = input()
    if("run" in p) and (("browser" in p) or ("explorer" in p)):
        print("Opening a Browser!")
        os.system("iexplore")
    elif("run" in p) and (("notepad" in p)or("editor" in p)):
        print("Opening Text Editor! ")
        os.system("notepad")
    elif("run" in p) and ("chrome" in p):
        print("Opening the Chrome Browser")
        os.system("chrome")
    elif("calculator" in p):
        print("Opening Calculator")
        os.system("calc")    
    elif("run" in p) and (("jupyter" in p)or("IDE" in p)):
        print("Opening Jupyter IDE")
        os.system("jupyter notebook")
    elif("run" in p) and (("paint" in p) or ("mspaint" in p)):
        print("Opening Paint Software!")
        os.system("mspaint")
    elif("run" in p) and (("mediaplayer" in p) or ("musicplayer" in p) or ("songplayer" in p)):
        print("Opening Media Player!")
        os.system("wmplayer")
    elif("run" in p) and ("gitbash" in p):
        print("Opening Git Bash")
        os.system("git bash")
    elif(("show" in p)or("listout" in p))and("directory" in p):  
        print("We are Listing all the directories...")
        os.system("dir")
        
    elif(("stop" in p) or ("exit" in p)):
        print("I am closing the program!")
        print("Bye! Come back again")
        os.system(exit())
        break
