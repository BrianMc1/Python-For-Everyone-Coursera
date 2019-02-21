def ComputePay(hours,rate):
    if hours <= 40:
        return(hours * rate)
    else :
        overtime = hours - 40
        return((40 * rate) + (overtime * (1.5 * rate)))

hours = input("How many hours my dude?")
hours = float(hours)
rate = input("And the rate is:")
rate = float(rate)

total = ComputePay(hours,rate)
print(total)
