#functions that add 2 numbers
def add(x, y):
    print(x + y)


add(3,21)
#function that subtarcts 2 numbers
def subtract(x, y):
    print(x - y)


subtract(3,21)
# function that multiplies 2 numbers
def multiply(x, y):
    print(x * y)


multiply(3,21)
#functions that divides 2 numbers 
def divide(x, y):
    print(x / y)


divide(28,14)

add(23,7)
subtract(19,7)
multiply(12,12)
divide(6,3)


x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))

print("Welcome to the majestic calc app!!!")
print("What would you like to do?")
print("Type (a)dd (s)ubtract (m)ultiply (d)ivide (q)uit")
user_choice = input(": ")
while(True):
    if user_choice == 'a':
        add(x,y)
# elif s
    elif user_choice == 's':
        subtract (x,y)
# elif m
    elif user_choice == 'm':
        multiply(x,y)
# elif d
    elif user_choice == 'd':
        divide(x,y)

# elif q
    elif user_choice == 'q':     
        print("shutting down")
    break

# break
# shutting down
# else
# invalid input