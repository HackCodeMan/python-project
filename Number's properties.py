#Import modules
import random
from time import sleep
#descriptions functions
def thinks ():
    for i in range(3):
        print("hm"+("."*(i+1)))
        sleep(1)
    print("I understand:)")
    sleep(1)
def give_me_number(a,b):
    """Chance a random number in range from 'a' to 'b' in variable 'number'"""
    global number #Accessing a global variable, now I can change the global variable outside the function
    number = random.randint (a,b)
def define_number_properties (number):
    """define number properties"""
    #How many digit?
    num_of_symbol = len(str(number))
    #Check number ends in zero or no
    ends_in_zero = False
    if (number % 10) == 0:
        ends_in_zero = True
    #What numbers in the range is a multiple of number
    multiples = []
    for i in range(number):
        if (number % (i+1)) == 0:
            multiples.append(str(i+1))
    return num_of_symbol,ends_in_zero,multiples
#Main part
chance = None
while chance != "1" and chance != "2":
    print("1 - User enters himself\n2 - program chance a random number")
    chance = input("Enter your chance: ")
if chance =="2":
    print("I guessed the random number and define his properties")
    print("Write me range:")
    range_from = int(input("From: "))
    range_to = int(input("To: "))
    print("I think what number to guess, wait")
    thinks()
    give_me_number(range_from,range_to)
else:
    print("I define number properties")
    number = int(input("Enter the number: "))
print("I am defining number properties, wait")
thinks()
num_of_symbol,ends_in_zero,multiples = define_number_properties(number)
if ends_in_zero:
    answer = "ends in zero"
else:
    answer = "don't ends in zero"
print("Number is ",num_of_symbol,"-digit","\nAnd this number ",answer,sep = '')
print("Multiples: "+ ", ".join(multiples))
print("This number is",number)
input("\n\nClick 'Enter' to exit")



