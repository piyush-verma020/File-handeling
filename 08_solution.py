# Q8> Write a program to make a copy of a text file "copy.txt".

with open("file.txt","r") as f:
    line = f.read()

with open("copy.txt","w") as f:     
# Evem if there was no file named for exaple copy.txt was present it would create a file with the same name and it will write the txt of the file which was copied
    f.write(line)