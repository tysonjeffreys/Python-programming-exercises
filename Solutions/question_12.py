'''
Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

numbers = list(range(1000, 3001))
evenNumbers = []
for number in numbers:
    if number % 2 == 0:
        evenNumbers.append(str(number))

print(','.join(evenNumbers))