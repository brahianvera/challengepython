number = 6
factorial_number = 0
for i in range(number+1):
    if(i == 0):
        factorial_number = 1
        continue
    factorial_number = factorial_number * i
print(factorial_number)