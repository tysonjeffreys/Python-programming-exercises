number = int(input("Please enter a number to factor."))
factors = [1]
i = 0
for x in range(1, number + 1):
    y = x * factors[i]
    factors.append(y)
    i = i+1
print(factors[-1])