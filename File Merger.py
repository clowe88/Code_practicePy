#File Merger
import glob
#file list
files = glob.glob("Dictionary\/all\/*.txt")
#file to merge into
master = open("Dictionary\/all\/MasterDictionary.txt", "a+")

#opens files and writes them to master file. 
for name in files:
    with open(name,"r") as file:
        contents = file.read()
        master.write(contents)
#closes master file. 
master.close()
    


print (master)