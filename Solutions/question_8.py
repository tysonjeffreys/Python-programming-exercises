'''
Question 8
Level 2

Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''


#this is my first solution

words = input("Please enter a list of words separated by commas: ")
wordsList = sorted(words.split(','))
sortWords = ','.join(wordsList)
print(sortWords)

#and my alterations after reading the given solution

wordsList = [x for x in input("Please enter a list of words separated by commas: ").split(',')]
wordsList.sort()
print(','.join(wordsList))
