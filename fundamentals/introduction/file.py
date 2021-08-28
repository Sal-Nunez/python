num1 = 42 # variable declaration, initialize number
num2 = 2.3 # variable declaration, initialize number
boolean = True # variable declaration, initialize boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, initialize tuples
#setting variables
print(type(fruit)) # print type of argument
print(pizza_toppings[1]) # print argument at index 1
pizza_toppings.append('Mushrooms') #add mushrooms to end of the list
print(person['name']) # print the name of argument
person['name'] = 'George' # change value dictionary
person['eye_color'] = 'blue' # add value dictionary
print(fruit[2]) # print argument at index 2

if num1 > 45: # conditional if
    print("It's greater") # print string if, if statement is yes
else: # conditional else
    print("It's lower") # print string if, if statement is no

if len(string) < 5: # conditional if, get length of argument
    print("It's a short word!") # if argument length is less than 5 print this
elif len(string) > 15: # conditional else if, get length of argument
    print("It's a long word!") # if argument length is more than 15 print this
else: # conditional statement else, if no if or else if statement is true then do this
    print("Just right!") # print this

for x in range(5): # for loop, starting from 0 up to but not including 5
    print(x) # print 0, 1, 2, 3, 4
for x in range(2,5): # for loop, starting from 2 and up to but not including 5
    print(x) #print 2, 3, 4
for x in range(2,10,3): # for loop starting from 2 up to but not including 10 by multiples of 3
    print(x) # print 2, 5, 8
x = 0 #variable declaration, setting a number
while(x < 5): # conditional while, loop from 0 until x is no longer less than 5
    print(x) # print 0, 1, 2, 3, 4
    x += 1 # add 1 to x every loop

pizza_toppings.pop() # remove last variable from list
pizza_toppings.pop(1) # remove variable at index 1 from list

print(person) # print dictionary person
person.pop('eye_color') # removes the key in dictionary person
print(person) # prints dictionary person

for topping in pizza_toppings: # conditional for loop, setting argument, pulling from list pizza_toppings
    if topping == 'Pepperoni': # conditional if, if argument is equal to pepperoni
        continue # continue loop and do nothing else
    print('After 1st if statement') #print string if argument isn't pepperoni or olives
    if topping == 'Olives': # if argument is equal to olives stop loop
        break

def print_hello_ten_times(): #defining a function
    for num in range(10): # range from 0 and up to but not including 10
        print('Hello') # print hello 10 times

print_hello_ten_times() #calling function ^^^^

def print_hello_x_times(x): # defining a function, setting argument
    for num in range(x): # sets the function to run argument amount of times
        print('Hello1') # print hello x = 4 times

print_hello_x_times(4) # calling function, sending parameter

def print_hello_x_or_ten_times(x = 10): # defining a function, setting argument, set argument to 10 if no parameter was sent
    for num in range(x): # sets the function to run argument amount of times
        print('Hello') # print hello x amount of times

print_hello_x_or_ten_times() # calling function, no parameter so argument will = 10
print_hello_x_or_ten_times(4) # calling function, sending parameter


"""
Bonus section
"""

# print(num3) # print argument
# num3 = 72 # variable declaration, initialize number
# fruit[0] = 'cranberry' # replace the fruit at index 0 of fruit with the string 'cranberry'
# print(person['favorite_team']) # print value of favorite team of argument person
# print(pizza_toppings[7]) # print the value at index 7 of pizza_toppings
#   print(boolean) # print the argument
# fruit.append('raspberry') # add raspberry to the end of the list fruit
# fruit.pop(1) # remove the value at index 1 of list fruit