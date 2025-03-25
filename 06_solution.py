# Q6> Write a program to mine a log file and find out whether it contains the word 'Python'.

word = input("Enter the word you wish to look for: ")
with open("log.txt","r") as f:
    line = f.read()
    if(word.lower() in line.lower()):
        print("Yes the word is present in the log file")
    else:
        print("There is no such word found in the log file")