#Write a program which reads user input until they say done
#Then print largest and smallest numbers

largest = None
smallest = None
while True:
    CurrentValue = input("Enter a number: ")
    if CurrentValue == 'done':
        break
    else:
        try:
            CurrentValue = int(CurrentValue)
            if largest == None:
                largest = CurrentValue
            elif CurrentValue > largest:
                largest = CurrentValue
            if smallest == None:
                smallest = CurrentValue
            elif CurrentValue < smallest:
                smallest = CurrentValue
            
        except:
            print('Invalid input')
            continue
print('Maximum is ',largest)
print('Minimum is ',smallest)
