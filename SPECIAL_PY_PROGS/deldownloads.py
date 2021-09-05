import os
dir = 'C://Users//home//Downloads'
files = os.listdir(dir)
for fil in files:
    if fil == ".tmp.drivedownload":
        files.remove(".tmp.drivedownload")
        continue
    elif fil == "desktop.ini":
        files.remove("desktop.ini")
        continue
    elif fil == "z.exe":
        files.remove("z.exe")
        continue
    else:
        os.remove(dir + "//" + fil)
        print()
        print("files deleted are : ")
    print(fil)