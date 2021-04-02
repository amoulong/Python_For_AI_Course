#reading files
file1= open("D:/HOMEWARE/Projets/Python_For_AI_Course/file.txt","w")
print(file1.name)
print(file1.mode)
print(file1.dir())
file1.writelines("ddsnjdsfjsjnvjdsqn \nhvdhjdbfjkaje22156e156e")
file1.close()


#secured mode to manage a file

with open("D:/HOMEWARE/Projets/Python_For_AI_Course/file.txt","r") as file1:
    fileContent=file1.read()
    print(fileContent)
#verification si fichier fermé
print(file1.closed)

#read and print only one line
with open("D:/HOMEWARE/Projets/Python_For_AI_Course/file.txt","r") as file1:
    fileContent=file1.readline()
    print(fileContent)
    #read the 15 first characters of a the next line
    fileContent=file1.readline(15)
    print(fileContent)