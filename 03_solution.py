# Q3> Write a program to generate multiplication tables from 2 to 20 and write it to the different files in a folder for a 13-year old.

def tables(n):
    table = ""
    for i in range(1,11):
        table += f"{n} * {i} = {n*i}\n"
    with open(f"table/table_{n}.txt","w") as f:
        f.write(table)

num1 = int(input("Enter the starting number of the multiplaication table: "))
num2 = int(input("Enter the last number of the multiplication table: "))
for i in range(num1,num2 + 1):
    tables(i)
