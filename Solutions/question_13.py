'''
Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

sentence = input('Please enter a sentnce with characters and digits: ')
elem = list(sentence)
print(elem)
charElem = []
numElem = []
for element in elem:
    if element.isdigit():
        numElem.append(element)
    elif element.isalpha():
        charElem.append(element)
        
print("LETTERS: " + str(len(charElem)))
print("NUMBERS: " + str(len(numElem)))
        