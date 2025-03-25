# Q7> Write a program to find out the line number where python is present in question number 6.

word =input("Enter the word you are looking for: ")
with open("log.txt", "r") as f:
    line = f.readline()
    index = 1
    print("\n")

    while (line != ""):
        if(word.lower() in line.lower()):
            print(f"The word {word} was found in {index} index")
        index +=1
        line = f.readline()
print("\n")
print("END")