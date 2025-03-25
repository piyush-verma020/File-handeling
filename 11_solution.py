# Q11> Write a program to rename a file to "renamed_by_python.txt".

with open("copy.txt",'r') as f:
    data_original = f.read()

with open("renamed_by_python.txt",'w') as f:
    f.write(data_original)

# Since renaming a file was not possible but we could just copy the data from the existing file and re-write it to a new file with the  desired file name 
# We ccould also use shutil and os module to remove the original file
# For now the work is done.