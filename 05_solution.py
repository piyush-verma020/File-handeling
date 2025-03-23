# Q5> Repeat the program 4 for a list of such words to be censored.

word = []
for i in range(3):
    keys = input("Enter the words which are to be censored: ")
    word.append(keys)

with open("censor.txt","r") as f:
    data = f.read()

for words in word:
    data = data.replace(words, "#" * len(words))

with open("censor.txt", "w") as f:
    f.write(data)