import sys

numbers = sys.argv[1].split(",")
targetNumber = sys.argv[2]


for number in numbers:
    for n in numbers:
        add = int(number) + int(n)
        if(add == int(targetNumber)):
            print(number,n)
            numbers.remove(number)
