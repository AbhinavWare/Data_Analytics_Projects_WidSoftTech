# Starts with variables used to store data or values which are used in operations and can be reused in programs.

#P.S Uncomment any instruction to execute.

# name=input("Enter your name:")

# name is variable "Abhinav" is string value stored in string variable. 
# Python automatically detects data type of variable based on value stored. 
# print(name)
# prints parameter provided in () onto console screen.

# print(type(name))
#type() function prints or returns the data type class of variable belonging to.

# marks=10
# print(marks) 
# print(type(marks))

# marks=input("Enter your marks:")
# print(marks)
# print(type(marks))

# a=0
# isZero=False
# if a==1:
#     isZero = True
# else:
#     print(isZero)
# print(isZero)r marks:")
# print(marks)
# print(type(marks))

# print("Java","C++","C",sep='-') #Can use -,_ ,etc.
# #sep stands for seprator which seprates the , text in print function using the symbol or data assigned to sep= and seprates text. 

# #All the above code was written on 09.06.2026.







# Below code is written on 10.06.2026.

#Operators.
# a=10
# b=20

#Arithematic operators perform mathematical caluclations on operands or variables values.
# print(a+b) #Addition of variables.
# print(a-b) #Subtraction of variables.
# print(a*b) #Multiplication of variables.
# print(a/b) #Division of variables.
# print(a%b) #Modulo division of variables. Returns reminder of division.
# print(a // b) #Floor division of variables . Rounds result to near whole number.
# print(a**b) #Exponent multiply of variables.

#Assignment operator are used to assign values '=' as well as can be used with arithematic operators to compute and assign result.
# c=30.5 #Assign
# print(c)

# c+=a #adds value of a to c and assign it to c.
#Use with aritehmatic op.
# print(c)

#Comparison operator compares two operators , checks their reilation and returns true or false based on condition.
# Comparison Operators.

# print(10 == 10)  # Equal to
# print(10 != 5)   # Not equal to
# print(10 > 5)    # Greater than
# print(10 < 20)   # Less than
# print(10 >= 10)  # Greater than or equal to
# print(10 <= 15)  # Less than or equal to

# Logical Operators.
# print(not True)  # Logical NOT reverts values and conditions. 
# print(True and False)  # Logical AND

# age = 25
# salary = 40000
# print(age>21 and salary > 20000)

#Identity operator is and is not which checks if it belongs to same identifier. Check if two operands belong to same object in memory.

# x = [1,2]
# y=[1,2]
# z=x
# print(y is x) #False because y and x are different objects in memory even though they have same values.

# print(x is y) #False because x and y are different objects in memory even though they have same values.
# y=x
# print(x is y) #True because x and y are now same objects in memory after assignment.
# print(x==y) #True because x and y have same values. == checks for value equality while is checks for identity of objects in memory.

#Membership operator checks if a value is present in a sequence or not.
# print(5 in [1,2,3,4,5]) #True because5 is present in the list.
# print(10 in [1,2,3,4,5]) #False because 10 is not present in the list.
# print(2 not in [1,3,4,5]) #True because 2 is present in the list.
#'0 and only 0' denoted false and any integer,float value denote true boolean values.






# Below code is written on 11.06.2026.

#Conditional Statements.
#These are statements or instructions used to compare variables oprands and execute statements based on condition.

#if else : 
#Syntax : if conition : ':' is mandatory.
            #Executes if true.
            #else:
                # These statements are executed. Intend is also important.
    
# age = 18
# if age>18:
#     print("You are adult!")
# else:
#     print("You are not adult!")
    
#Only if can also work but to apply logic properly and eliminate the cavet if logic (condition) becomes false then we manditorily use if-else.
#else can only be use with if and not without it.
 
#else-if or elif: is used in if block to check multiple conditions and onluy one if elif or else if present is executed rest all are ignored based on conditions result.
#else is optional in elif.
# grade = int(input("Enter your grade:"))
# if grade>90 :
#     print(grade, "is excellent!")
# elif grade>=80:
#     print(grade, " is good!")
# elif grade >= 70:
#      print(grade, " is average!")
# else:
#      print("you got distinction!")
     

# age = 19
# has_ID=True

# if age>=18:
    
#     if has_ID:
#         print("Eligible to vote!")
#     else:
#         print("Make ID")
#         has_ID=True
# else:
#     print("Ineligible to vote!")
    
#Shorthand if is also allowd like.
# name="Abhinav"
# if name == "Abhinav" : print(name)

#Shorthand if else is also allowed.
#Here first if code is given seprated by if statement to check and then else statement.
# marks = 90
# print("Marks are 90!") if marks == 90 else print("Marks are less or greater than 90!")
#Select or match(Switch) case in py where based on value of one variable the condition or cases are 
#executed. They work similarly like if elif. It is used when we want to execute a case based on value of variable or boolean condition.
# day = 3
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case _:
#         print("Invalid entry!")
    
#_: is default case which is executed when no case value matches variables value in match case.
#We can also add "|" "or" "and" operators.
# age = 18
# match age:
#     case x if x>=18:
#         print("Adult!")
#     case x if x < 18:
#         print("Not adult!")











#Below code is written on 12.06.2026.
#Loops are used to iterate through list, strings and other structures as well as to repeat varied statements written inside loop.
#Loop to iterate list,set.

#for loop takes an itreator variable and use in with a list or identifier to iterate over or use range() function.

# num=[1,2,3,4]
# n={1,2,3,4}
# for i in num:
#     print(i,end=" ")
# for i in n:
#     print(i,end=" ")
#Tuple.
# n1=(1,2,3,4,5)
# for i in range(6,0,-1): #or to gor from 0->6 use range(0,6,1):
#     print(i,end=" ") #Reverse. range(start,stop,step) step means iteration numbners to go from start to stop.
    
# for i in n1:
#     print(i,end=" ")
    
# for i in range(1,5,1):
#     for j in range(1,i):
#         print("*",end=" ")
#     print()

# for i in range(1,5):
#     print("*" * i)

# for i in range(0,11,2): #prints even numbers for odd use range(1,11,2): starting point says all.
#     print(i,end=" ") # also can use if i%2==0: print(i,,end=" ") with range(11).
    
#Table print.
# num=int(input("Enter number to print table:"))
# for i in range(1,11,1):
#     print(i*num)

#while loop takes a condition and based on condition being true executes the loop and statements until it becomes false.

# i = 5
# while i < 10:
#     print(i,end=" ")
#     i+=1 # or use i>1 and i-=1
    
#Even odd.
# nums = [1,2,3,4,5]
# i=0
# num=0
# while i < len(nums) :
#     num=nums[i]
#     if num%2==0:
#         print(num , "is Even")
#     else:
#         print(num,"is Odd")
#     i+=1


#Break statement is used to break iteration and based onn condition in loop to break loop.
# while True:
#     name = input("Enter name:")
#     if name == "Abhinav":
#         break
    
#Continuse statement is used to skip a loop iteration based on condition where ever it is used that iteration is skiped and loop is continued from next  iteration.
# while True:
#     name = input("Enter name:")
#     if name == "Abhinav":
#         continue
#     else:
#         print(name)

#Pass statement is used when we want to totally skip full execution of loop where we want that loop or if else statement in future or further use 
#for same we use it to make logic flow properly.
# num = [1,2,3,-1,-2,5]
# for i in num:
#     if i<0:
#         pass #It ignores the -ve nums.
#     else:
#         print(i)
    
#enumerate function is used to print both index and value in structures like list,tuple,set,etc. it returns the index and value at index.
# grade = ['A','B','C','D']
# for i,v in enumerate(grade):
#     print(i,v)
    
#zip() is used to combine two structures like list, set ,etc. to manipulate them or to process them.
# marks = [90,80,70,60]
# grade = ['A','B','C','D']
# for m,g in zip(marks,grade):
#     print(m,g)
    
#We use f string function to print variable values directly in strings or use variables dirctly in strings.
# a=10
# b=20
# print(f"Multiplication of {a} and {b} = {a*b}")
#Nested loops are loops inside other loops used in patterns and complex computations.
# for i in range(1,4):
#     for j in range(1,11,1):
#         print(f"{i} x {j} = {i*j}")
#     print()
#Printing tables using nested for loop.

#Patterns.
# for i in range(1,5):
#     for i in range(i):
#         print("*",end=" ")
#     print()










#This code is written on 15.06.2026.

#Pyramid and dimond pattern.
# n = 6
# for i in range(1,n+1):
    
#     for j in range(n-i):
#         print(" ",end = "")
#     for k in range(2*i-1):
#         print("*", end="")
#     print()
#     # print(" ",end= "")

# # print(" ",end="")
# for i in range(n-1,0,-1):
    
#     for j in range(n-i):
#         print(" ",end = "")
#     for k in range(2*i-1):
#         print("*", end="")
    # print()
    
    
    
#Floyd traingle.
# for i in range(1,6):
#     for i in range(1,i+1):
#         print(i,end="")
#     print()
# for j in range(6,0,-1):
#     for j in range(1,j+1):
#         print(j,end="")
#     print()


#Table multplication.

# for i in range(1,4):
#     for j in range(1,11):
#         print(f"{i} x {j} = {i*j}")








#This code is written on 16.06.2026.

#Functions
#These are resuable block of code that are used to perform specific task.
#These create modularity.
#There are 4 types of functions:
#They are defined used def keyword. A function can be of a class or independent. Function can either take one or more parameters or also can have no parameters.


# def greet(name): This is parameter. where arguments are passed. These are essientially variables.
#     print("Welcome!",name)
# name = input("Enter your name:")
# greet(name) #This is arguement.

# def add(a,b,c): #Multiple parameters.
#     return a+b+c #Function can or cannot either return value based on logic.
# print(add(1,2,3)) 


#Default Arguments in function.
#These are arguments or parameter which are initialized inside argumment list using assignment operator. Same as we use variables.
# def cityName(cityN = "Nagpur"):
#     return cityN #We can also have multiple values seprated by ','.
# print("With default arguments:",cityName())
# print("Without default arguments:",cityName("Pune")) #Also can pass parameters like normal functions.
# #These allow us to call function having arguments withhout or with parameters.


#Key word arguments in functions.
# Keyword arguments (also called named arguments) are values passed to a function by explicitly specifying the parameter name along with the value in the format parameter_name = value.
# def kwargs(name,age,city):
#     print(name,age,city)
# kwargs(name = "Abhinav",city = "Nagpur", age = 18)


#Arbitary arguments in functions. (*args)
#These are defined using start * where we dont know exact how many parameters we need to pass to function.
# def total(*marks): #we can take any N amount of marks.
#     sum = 0
#     for i in marks:
#         sum += i
#     return sum
# print("Total of marks:",total(100,99,97,93,98,100))


#**Arbitary arguments in functions. (**kwargs)
#These are same as above for keyword arguments used where we dont know exact amount keyword arguments the function will take.
# def dataDisplay(**data):
#     print(data)
# dataDisplay(name = "Abhinav", city = "Nagpur", age = 18) #It considers data in dictionary key-value pair format and in dict format prints output.


#P.S :  Method overloading or function overloading is not available in python. It can be implemented using *args and **kwargs.

#The return keyword is used within functions where we want to return values from function this is optional based on logic of function. 
#But for some scenarios 'returning values' from function is usefull. It can also be used stand alone like only 'return'.


# Returning multiple values from function.
# def calc(a,b):
#     return a+b,a-b
# print(calc(10,20)) #It returns output in form of tuples.
# #Also same.
# c,d = calc(50,60) #Python assigns c result returned throgh a +b and b to a-b. 
#If only a is printed only result of a+b is printed same if only b is printed returning a-b.
#If result = calc(10,20)
#print(result) prints (30,-10) as it is assigned full result of function.
# print(c,d) #Dos'nt return in tuple due to it is assigned before. 


#Local variables are variable only visible, alive or usable in function it's scope is only inside it and it cannot be accessed or used outside function.
#On the other hand normal variables are global and accessed anywhere in program.


#Python allows us to have nested functions like nested if-else and loops.
# def outer():
    
#     print("This is outer function!")
#     def inner(): #Can only be used, accessed or called inside outer function.
#         print("This is inner function!")
#     inner()    
# outer()
# inner() cannot be called due to local scope.
#The parameters can also only  be passes through outer function to inner one.


#Reccursion or recurrcive function.
#This function calls itself inside the function repersenting a loop like execution of function to solve problems through smaller instance of same problem.

# def countdown(n):
#     if n == 0:
#         return
#     print(n)
#     countdown(n-1) #Decreases value of n by 1.
    
# countdown(5)

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n*factorial(n-1)
# n = int(input("Enter number to find factorial:"))
# print(f"Factorial of {n}:",factorial(n))

# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# term = int(input("Enter number to find fibonacci series:"))
# for i in range(term):
#     print(fib(i),end=" ")
# print(fib(term))










#This code is written on 17.06.2026.
#List : A data structure that stores elements in ordered way and is mutable i.e. changable. Represented using[].
#List is in format : list[Start index: Stop index: Step index] like for loop.

# list = [1,2,3,4]

#List Slicing: Access list elements using index. Slicing can be done -1 from last element from list and 0 from front.
# print(list[0]) #Positive slicing.
# print(list[-1]) #Negative slicing, gets from end.

# print(list[1:4])
# print(list[0:3])
# print(list[::2]) #Returns or prints alternate elements.
# print(list[-1:-4])
# print(list[::-1]) #Reverses list.

# list[2] = 10 #Modifying  list at index 2 replacing 3 with 10.
# print(list) 

#append(): appends data or inserts data at end of current list.
# list.append(50)
# print(list)

#remove() : Like append we can also remove data from list based on index or value(entry) we want to remove.
# list.remove(list[4]) #Remove by index.
# print(list) 

# list.remove(10) #Remove by value.
# print(list)

#len(): Returns length in int of list i.e. amount of elements.
# print(len(list))

#copy(): Copies one list's elements or data to other.
# list2 = [] #Creates empty list.
# list2 = list.copy()
# print(list2)

#Using for loop in list.
# for l in list:
#     print(list)
    
# list = [1,2,3,4]
# count = 0
# for item in list:
#     count+=1

# print("Total list elements:",count)

# max = list[0]
# for i in list:
#     if i > max:
#         max= i
        
# print("Max number:",max)

# square = []
# for i in range(1,11):
#     square.append(i**2)
# print("List of squares:",square)


# sum = 0
# for n in list:
#     if n % 2 == 0:
#         sum+=n
# print("Sum of list elemenets:",sum)
       
# numbers = [10, -5, 20, -8, 15, 0, -2]
# new_list = []
# for num in numbers:
#     if num >= 0:
#         new_list.append(num)

# print("Original list:", numbers)
# print("New list:", new_list)

# list = [1,2,3,4,5]

# list.sort() 
# print(list[-2])
# rev_l = []
# for i in range(len(list)-1,-1,-1):
#     rev_l.append(list[i])
# print("Reversed list:",rev_l)


# my_list = [1,2,3,4]
# largest = my_list[0]
# second = my_list[0]
# for i in my_list:
#     if i > largest:
#         second = largest
#         largest = i
#     elif second < i and i!=largest:
#         second = i 
# print("Second largest number:",second)
