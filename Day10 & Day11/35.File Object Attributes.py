fr = open("FileContent.txt","r")
print("File name:",fr.name)
print("Access mode:",fr.mode)
print("Closed?",fr.closed)
fr.close()
print("After closing the file, closed?",fr.closed)