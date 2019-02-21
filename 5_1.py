#Write a program which reads user input until they say done
#Then print sum, count, and average variables

flag = None
sum = 0.0
count = 0
while flag is None:
    CurrentValue = input("Enter a number: ")
    if CurrentValue == 'done':
        #break
        flag = 'GetOuttaHere'
    else:
        try:
            CurrentValue = float(CurrentValue)
            sum = sum + CurrentValue
            count = count + 1
        except:
            print('Invalid input',CurrentValue,type(CurrentValue))
            continue
print(sum,count,sum/count)
