#Write a program which accepts a sequence of comma-separated numbers from console and generate a list 
#and a tuple which contains every number.
#Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#Then, the output should be:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')


string = input("Enter numbers separated by commas: ")

string_list = string.split(',')
string_tuple = tuple(string_list)
print(string_list)
print(string_tuple)
