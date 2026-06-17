#Task 1: Create a function to print your name.
def greet(name):
    return f"Hello {name}!"
name = input("Enter your name:")
print(greet(name))


#Task 2: Create addition function with two parameters.
def add(a,b):
    return a+b
n1 = int(input("Enter a digit:"))
n2 = int(input("Enter another digit:"))
print(f"Addition of {n1} + {n2}:{add(n1,n2)}")


#Task 3: Create multiplication function using return.
def multiply(a,b):
    return a*b
print("Multiplication of 10 and 20:",multiply(10,20))


#Task 4: Create function to find square of number.
def sqr(num):
    return num*num
n1 = int(input("Enter a digit:"))
print(f"Square of {n1} : {sqr(n1)}")


#Task 5: Create function with default parameter.
def nameDisplay(name="Abhinav"):
    print(name)
nameDisplay()
nameDisplay("Asky")


#Task 6: Create calculator using functions.
def calculator(a,b,op):
    
    
    if op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/":
        if num2 == 0:
            print("Divide by zero error!")
        else:
            print(a/b)
    elif op == "**":
        print(a**b)
    else:
        print(a//b)
num1 = int(input("Enter a digit:"))
num2 = int(input("Enter another digit:"))
op = input("Enter operation(+,-,/,*,**,//)")
calculator(num1,num2,op)


#Task 7: Create function to find largest of 3 numbers.
def largest(a,b,c):
    if a > b and a>c:
        print(f"{a} is greatest!")
    elif b>a and b>c:
        print(f"{b} is greatest!")
    else:
        print(f"{c} is greatest!")
largest(10,20,30)


#Task 8: Create recursive factorial function.
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)
    
num = int(input("Enter number:"))
print(f"Factorial of {num}:",fact(num))


#Task 9: Create function using *args to calculate sum.
def sum(*num):
    sum = 0
    for i in num:
        sum+=i
    return sum
print("Sum of 10,20,30,40,50:",sum(10,20,30,40,50))


#Task 10: Create function using **kwargs to store student details.
def studentDisplay(**data):
    print(data)
print(studentDisplay(name="Abhianv",age=17,city="Nagpur",collage="GPN"))