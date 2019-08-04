#Write a program that will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers should be printed in a comma-separated sequence on a single line.


numbers = []
for x in range(2000, 3201):
    if x % 7 == 0:
        if x % 5 != 0:    
            numbers.append(str(x))

print(','.join(numbers))


