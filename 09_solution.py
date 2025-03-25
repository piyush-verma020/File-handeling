# Q9> Write a program to find out whether a file is identical & matches the content of another file.

with open("file.txt","r") as f:
    data1 = f.read()

with open("copy.txt","r") as k:
    data2 = k.read()

if(data1 == data2):
    print("YUP! Both of the mentioned files have the same content in it")
else:
    print("NOPE! Both of the files have their own unique contents")