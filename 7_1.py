# Write a program that prompts for a file name, then opens that file and 
# reads through the file, and print the contents of the file in upper case. 
# Use the file words.txt to produce the output below.

FileName = input('Enter the file name: ')
FileContents = open(FileName)
for line in FileContents:
    line = line.rstrip()
    line = line.upper()
    print(line)

# you can also do print(line.upper())