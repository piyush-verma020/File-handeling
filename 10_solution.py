# Q10> Write a program to wipe out the content of a file using python.

with open("file.txt","r") as f:
    data = f.read()
    new_data = data.replace(data,"")

with open("file.txt","w") as f:
    f.write(new_data)

# OR 
# You could just use this method :->

with open("file.txt","w") as f:
    f.write("")