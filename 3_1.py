hours = input("How many hours my dude?")
hours = float(hours)
rate = input("And the rate is:")
rate = float(rate)
total = -1
overtime = 0

if hours <= 40:
    total = hours * rate
else :
    overtime = hours - 40
    total = (40 * rate) + (overtime * (1.5 * rate))
print (total)
