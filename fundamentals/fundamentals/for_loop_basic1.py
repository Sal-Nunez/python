for x in range(151):
    print(x)
for x in range(5, 1001, 5):
    print(x)
for x in range(1, 101):
    if (x % 10 == 0) and (x % 5 == 0):
        print("Coding Dojo")
    elif (x % 5 == 0):
        print("Coding")
    else:
        print(x)
sum = 0
for x in range(500001) :
    if (x % 2 == 1):
        sum += x
    elif (x == 500000):
        print(sum)
for x in range (2018, -1, -4):
    print(x)
def flexibleCounter(lowNum, highNum, mult):
    for x in range(lowNum, highNum+1):
        if (x % mult == 0):
            print(x)
flexibleCounter(2, 9, 3)