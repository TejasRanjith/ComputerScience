import os
dir = 'C://Users//home//Desktop//Desktop (2)//Screenshots'
for files in os.listdir(dir):
    print(files)
    if ".png" in files:    
        os.remove(dir + "//"+ files)
    else:
        continue