#Write a program that prompts for a file name, 
# then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and 
# compute the average of those values and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.

# file is mbox-short.txt

FileName = input('Please enter the file name: ')
FileHandler = open(FileName)
Counter = 0
Total = 0
for line in FileHandler:
    if line.startswith('X-DSPAM-Confidence:'):
        Counter = Counter + 1
        ZeroSpot = line.find('0')
        Total = Total + float(line[ZeroSpot:])
print('Average  spam confidence:', Total / Counter)

# could also do 
# for line in FileHandler:
#    if not line.startswith("X-DSPAM-Confidence:") : continue
#    lines 16-18 would go here
