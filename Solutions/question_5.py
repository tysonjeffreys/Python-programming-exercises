#Question 5
#Level 1

#Question:
#Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.

#Hints:
#Use __init__ method to construct some parameters

class StringStuff():
    
    def __init__(self, name):
        self.name = name
    
    def getString(self):
        print(self.name + ' please type something and press enter: ')
        self.string = input()
        
    def printString(self):
        print(self.string.upper())


name = input('What is your name? ')

first_string = StringStuff(name)

first_string.getString()



first_string.printString()