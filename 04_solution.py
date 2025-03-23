# Q4> A file contains a word "Donkey" multiple times. You need to write a program which will replace the word with #### by updating the same file.

import re

# Well the inport re allows us to import re.sub() which is a function from Python’s re (regular expressions) module that replaces the occurrences of a pattern in a string with a required replacement of a string 
word = input("Enter the word you wish to censor: ")

with open("censor.txt", "r") as f:
    data = f.read()  # It reads the entire file as once

# Replacing the word in a case-insensitive manner
censored_data = re.sub(word, "######", data, flags=re.IGNORECASE)

with open("censor.txt", "w") as f:
    f.write(censored_data)  # Writing the censored data back to the file
    