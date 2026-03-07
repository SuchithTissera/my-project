#You can do basic addition,substraction, multiplication and division
#def loops to do the operations
def addition():
    global value
    z = int(input("input the other number"))
    value += z

def substraction():
    global value
    z = int(input("input the other number"))
    value -= z

def multiplication():
    global value
    z = int(input("input the other number"))
    value = value * z

def division():
    global value
    z = int(input("input the other number"))
    value = value / z

value = 0
x = int(input("input a number?"))
value += x


#while loop to carry out operations until the user is finished
finished = 'no'
while finished == 'no':
    y = input("what operation do u want Eg : (+,-, *, /)")
    #if loops to see which operations need to be done
    if y == '+':
        addition()
    elif y == '-':
        substraction()
    elif y == '*':
        multiplication()
    elif y== '/':
        division()

    #a output to see the subtotals after each iteration
    print("current value:", value)

    finished = input("are you done? (yes/no): ")

#the final total 
print("final value:",value)
