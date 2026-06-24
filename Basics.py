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
#It allows repeated elements.

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

#remove() : Like append we can also remove data from list based on value(entry) we want to remove. Also can use index.
# list = [1,2,3,4]
# list.remove(list[-1]) #Remove by index.
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
#List comprehension: It provides a shorthand way to to implement for loop in list.
#It can also implement if-else all in one line.

# square = [x**2 for x in range(1,11)]
# print(square)

# nums = [1,2,3,4,5]
# even_odd = [f"{num} is Even!" if num%2==0 else f"{num} is Odd!" for num in nums]
# print(even_odd)









#This code is written on 18.06.2026.

#clear(): This is used to clear any data in list.
# list = [1,2,3,4]
# list.clear()
# print(list)

#count(): It helps to count elements of given value by returning the amount of elements in list.
#print(list.count(1)) #Counts are returns amount of 1's in list.

#extend(): It adds a specified list elements at end of list.
# l2 = [5,6,7,8]
# list.extend(l2) #Adds l2 elements to list.
# print(list) 


#index(): Returns first position of given value. As elements are repeated it returns index of first apperaing value.
# print(list.index(1))


#reverse(): Reverses order of elements in list.
# list.reverse() #Reverses list.
# print(list)

#sort(): Arrange elements in ascending or descending order.
# list.sort() #Sorts in ascending order.
# print(list)
# list.sort(reverse=True) #Sorts in descending order.
# print(list)

#pop(): Removes element at specified position.
# list.pop(-1) #Pops value at index -1 or n-1.
# print(list)

#Difference between remove() and pop() is that remove deletes by value and 

#1
# nums = [1,2,3,4,5,6,7,8]
# even_odd = [f"{n} is Even!" if n%2==0 else f"{n} is Odd!" for n in nums]
# print(even_odd)

#3
# l1 = [1,2,3,4,5]
# l2 = [4,5,6,7,8]
# common = [x for x in l1 if x in l2]
# print("Common elements:", common)
# print("Total common elements:", len(common))
#4
# list = [1,2,2,3,3,3,4,4,4,4]
# freq = {}
# for i in list:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i] = 1
# print(freq)
#5
# nums = [5, 2, 8, 1, 9]
# for i in range(len(nums)):
#     for j in range(len(nums) - i - 1):
#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]
# print(nums)
#6
# nums = [1, 9, 2, 8, 3, 7, 4, 6]
# target = 10
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] + nums[j] == target:
#             print((nums[i],nums[j]))
#6
# nums = [[1, 2], [3, 4], [5, 6]]
# flat = []
# for subl in nums:
#     for i in subl:
#         flat.append(i)
# print(flat)

#2
# num = [1,2,3,2,4,5,3,6]
# uk_list = []
# for i in range(len(num)):
#     count = 0
#     for j in range(i):
#         if num[i] == num[j]:
#             count+=1
        
#     if count == 0:
#         uk_list.append(i)
# print(uk_list)







#This code was written on 19.06.2026.

#Tuple is a collection of ordered and immutable data structure which allows duplicates.
#It is represented using() and any list or set,etc are casted to it using tuple(). It has similar working and functions like list.
#It's mainly made un-changable as it must be secures i.e. it is made to keep collectionn secure.
#It can contain values belonging to different types like combination of float, double,etc.

#Indexing works similar to lists.
# my_tup = (1,2,3,4,5)
# print(my_tup[1:4])
# print(my_tup[::2]) #Prints alternate elements
# print(my_tup[::-1]) #Reverses tuple

#my_tup[0] = 100 gives error but...
# print(id(my_tup))
# my_tup = (100,200,300,400,500) #Works as we resign all elements or any creating new tuple.
# print(my_tup,id(my_tup))

#Tuple allows ressignment, the only way to change tuples.

#Tuple concatination: Combining any two or more tuples using '+' operator.
# tup1 = (1,2,3,4)
# tup2 = (5,6,7,8)
# tup3 = tup1 + tup2
# print(tup3)
# print(tup1*3) #prints tup1 three times in form of tuple.

#We can use in and not in operators same as list directly. Same len() function also returns amount of elements like list.
#Also index function performs same way in list.

#Packed tuple: We can create tuples without () just by seperating elements using ',' like 10,20,30.. feature available for tuples.
# tup = 1,2,3,4
# print(tup)
# print(type(tup)) #Prints my tup.

#Anything inside () is considerd tuple even if there is single element.
# a = (10)
# print(a,type(a))

#Unpacking is when we assign multiple variables(tuple) a collection.
# a,b,c = (1,2,3) #Assigns a = 1, b = 2, c = 3 each
# print(a,b,c) 
#But for..
# x,y,*z = (10,20,30,40,50) #Assigns x and y only one variable as their capacity and z is varibale using '*' and all assignmenst woukd be adjusted using it.
# print(x," ",y," ",z)

# tup = (1,2,3,4,5)
# for i in tup:
#     print(i)
    
#First element.
# print(tup[0])
# print(tup[-1])

# count = 0
# for i in tup:
#     count+=1
# print("Elements in tuple:",count)

# find = int(input("Enter value to search:"))
# found = False
# for i in tup:
#     if i == find:
#         found = True
#         break
    
# if found:
#     print(f"{find} exists in:",tup)
# else:
#     print(f"{find} does not exists in:",tup)


# tuple = (1,2,2,3,3,3,4,4,4,4)
# freq = {}
# for i in tuple:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i] = 1
# print(freq)

# tup = (1,2,3,4)
# max = tup[0]
# for i in tup:
#     if i > max:
#         max = i
# print("Max value:",max)

# data = (10,20,30)
# a,b,c = data
# print(a," ",b," ",c)

# a = 1,2,3
# b = 4,5,6

# print("Before swapping:",a," ",b)
# a,b = b,a
# print("After swapping:",a," ",b)

# t = ((1,2),(3,4),(5,6))
# for inner in t:
#     for i in inner:
#         print(i,end=" ")
        
# tup = (1,2,3,1,2,3,4,5)
# unique = ()
# for i in tup:
#     found = False
#     for u in unique:
#         if i == u:
#             found = True
#             break
#     if not found:
#         unique += (i,)
# print("Orignal:",tup)
# print("Removing duplicates:",unique)








#This code is written on 22.06.2026.

#Set: It is collection of un-ordered, unique, mutable set of elements.
#It can only store data belongoing to int, float, string, tuple.
#This is also valid s1 = set([1,2,3,4]) or ((1,2,3,4)) where we cast a data structure to set using set().
#We use them to remove duplicates and to perform mathematical operations as well as to check membership checking.
#It dosnt allow indexing like tuple or list.

# s1 = {1,2,3,4}
#print(s1[1]) gives error.
#Allowed.
# print("{",end="")
# for i in s1:
#     print(i ,end=" ")
# print("}")

#add(): Used to add single element in set.
# s = {1,2}
# print(s)
# s.add(3)
# print(s)

#update(): Used to add more than one element in set.
# s.update([4,5,6,7,8,9,10])
# print(s)

#remove(): Removes single element from set a throws error when element not found.
#s.remove(11) Throws error.
# s.remove(1)

#discard: Same purpose as remove() but dosnt throw error.
# s.discard(22)

#pop(): Removes random element from set.
# s.pop()

# print(s)

#clear(): Same as list and tuple it deletes all elements of set.
# s.clear()
# print(s)

# Initializing sets
# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}

# 1. Union (All unique elements)
#print(set_a | set_b)          # Output: {1, 2, 3, 4, 5, 6}
#print(set_a.union(set_b))     # Output: {1, 2, 3, 4, 5, 6}

# 2. Intersection (Only common elements)
# print(set_a & set_b)          # Output: {3, 4}
# print(set_a.intersection(set_b)) 

# 3. Difference (In A but not B)
# print(set_a - set_b)          # Output: {1, 2}
# print(set_a.difference(set_b)) 

# 4. Symmetric Difference (In A or B, but not both)
# print(set_a ^ set_b)          # Output: {1, 2, 5, 6}
# print(set_a.symmetric_difference(set_b))


#Frozen set: A type of set which is immutable i.e. cant be changed after declaration and initialization.
# s = {1,2,3,4}
# s2 = frozenset(s)
# s2.add(1) Throws error.
# print(s2,type(s2))

# s1 = {1,2,3,4,5}
# s1.add(6)
# print(s1)
# s1.remove(6)
# print(s1)

# s2 = {6,7,8,9,10}
# print(s1 | s2) #union

# print(s1 & s2) #intersection.

# l1 = [10,20,30,40,10]
# s3 = set(l1)
# l2 = list(s3)
# print(l2)


#GFG problem.
# def setInsert(arr,n):
#     s1 = set(arr)
#     for i in range(n):
#         s1.add(arr[i])
#     return s1
# def setDisplay(s):
#     for i in s:
#         print(i,end=" ")
#     print()
# def setErased(s,x):
#     if x in s:
#         s.remove(x)
#         print(f"{x} erased!")
#     else:
#         print(f"{x} not found!")
# n = int(input("Enter size of arr:"))
# arr = []
# for i in range(n):
#     arr.append(int(input("Enter element:")))
# print(arr)
# s = set(arr)
# setInsert(arr,n)
# setDisplay(s)
# x = int(input("Enter element to erase:"))
# setErased(s,x)
# print(s)






#This code is written on 23.06.2026.

#Dictionary: It is a collection of data stored in key value pairs, it is unordered, mutable and can be indexed using keys.
# student = {"name":"Abhinav","Age":"18","City":"Nagpur","Course":["Eng","Math"]} we can also have list here.
# print(student) :Ex.

#For casting we use dict() to cast data structure to dictionary.
#It's main use is in API Data Model and structure where they are in json format in dictionary key-value pairs.

#Some dictionary assignments:
# d1 = dict(a=1,b=2,c=3)
# print(d1)

# d2 = dict([('a',1),('b',2),('c',3)]) #Tuple declaration.
# print(d2)

#Accessing values.
# student = {"name":"Abhinav","Age":"18","City":"Nagpur","Course":["Eng","Math"]}
# s1 = {}
# print(student["Course"][0]) #Access 'Eng'm from course.
# print(student["Age"]) #Access age.
# print(student.get('marks')) #.get() by passes error by accessing any key not available in dict. Used to check if any key exists like that or not which if not returns 'None'.
# student["name"] = "Aryan" #Changing values using keys.
# print(student["name"])
# student['marks'] = 92.68 #Adds new key-value pair.
# print(student)

#del : It deletes dictionary.
# del s1

#popitem() : Removes and returns the last inserted key-value pair as a tuple. From 3.7+ it removes last inserted item only.

#pop(key) : Removes the specified key and returns its value.

#clear() : Removes all items from the dictionar
# student1 = {"name":"Abhinav", "age":18, "city":"Nagpur"}
# print(student1.pop("age"))   # 18
# print(student1.popitem())    # ('city', 'Nagpur')
# student1.clear()
# print(student1)              # {}

#keys(): returns keys of specific dict. values(): Same as keys() by returns values of keys. items(): Returns both keys and values.

# s1 = {'name':"Abhinav",'age':18,'city':"Nagpur"}

# print(s1.keys()) #dict_keys(['name', 'age', 'city']) o/p.
# print(s1.values()) #dict_values(['Abhinav', 18, 'Nagpur']) o/p.
# print(s1.items()) #dict_items([('name', 'Abhinav'), ('age', 18), ('city', 'Nagpur')]) o/p.

# #Same use.
# for keys in s1:
#     print(keys,end=" ")
# print()
# for values in s1.values():
#     print(values,end=" ")
# print()
# for items in s1.items():
#     print(keys,values)

#Nested dict:
# student = {'s1':{'name':"Abhinav",'age':18,'city':"Nagpur"},'s2':{'name':"Abhinav",'age':18,'city':"Nagpur"}}
# print(student)
# print(student['s1']) #Access only s1.
# print(student['s1']['name']) #Access keys and values of inner dictionary s1.

# student = {}

# student["name"] = input("Enter name: ")
# student["age"] = int(input("Enter age: "))
# student["city"] = input("Enter city: ")

# print(student["age"])
# student['course'] = input("Enter course:")
# print(student["course"])
# student["city"] = "Pune"
# print(student["city"])
# print(student.pop('age'))

# print(student.items())

# key = input("Enter key to check:")

# print("Does any key exist:",student.get(key))

# word = "Banana"

# freq = {}
# for ch in word:
#     if ch in freq:
#         freq[ch]+=1
#     else:
#         freq[ch]=1
# print(freq)


# s1 = {'name':"Aryan",'age':18}
# s2 = {'name':"Soham",'age':18}
# print(s1 | s2) #Merge s1 and s2

# marks = {"math": 90, "eng": 80, "sci": 95}
# high = max(marks.values())
# print("Highest marks:",high)









#This code is written on 24.06.2026.

#Strings: A structure that can store sequecnce of characters represented by quotations (double mostly preffered).
#Way to write multi-line string.
# message = """Hello,Welcome 
# to python programming!"""
# print(message)

#In strings each character even white blank spaces have indexes.Pythone also allows negative indexing i.e. last element has index -1 and further on.
# str = "Data Analysis"
# print(str[0]) #D
# print(str[-3]) #S
# print(str[::-1]) #Reverses string.
# print(str[:4]) #Data
# print(str[5:]) #Analysis

#String repetetion: We can use '*' and times to repeat in print statements to repeat certain statements specially string.
# print("Hello! "*4) #Prints 'Hello!' 4 times without space.
#end= dosnt workk with string repeatetion.

#len() : Returns amount of characters in string including spaces.

#String concat: Used to combine two strings.
# s1 = "Hello "
# s2v = "World!"
# msg = s1 + s2v #Also can add something like " " in between.
# print(msg)

#Using in and not in (Membership operator) we can check if any string is in a string.
# msg = "Hello World!"
# s1 = "Hello"
# s2 = "Hi"
# print(s1 not in msg) #s1 is in msg.
# print(s2 in msg) #s2 not intt msg.


#Pattern print:
# for i in range(1,6):
#     print("*"*i)
# for i in range(5,0,-1):
#     print("*"*i)

#upper() : Converts all characters in calling string to upper case.
# str1 = "Hello"
# print(str1.upper())

#lower() : Converts all characters in calling string to lower case.
# str1 = "Hello"
# print(str1.lower())

#title() : It makes the first letter or charachter capital. It includes blank space also and makes first apperaing letter capital.

# s1 = "hello"
# print(s1.title())
# s2 = " hello" #Also makes h capital
# print(s2.title())

#capitalize() : In Python, string.capitalize() is a built-in method that converts the first character of a string to uppercase and all remaining characters to lowercase.
# s = "hEllO"
# print(s.capitalize())

#These are used to normalize case of data.

#swapcase() : It is used to swap cases of characters where the letters in uppercase are converted
#to lower case and lower to upper.
# s = "hEllO"
# print(s.swapcase())

#strip() : It removes extra space in strings.
# s = "    Python    "
# print(s.strip())

#lstrip() and rstrip() removes spaces from left and right.
# print(s.lstrip())
# print(s.rstrip())


#find() : Use the .find() method to get the starting index of the first occurrence. It returns -1 if the substring is not found, preventing program crashes.
# str = "Python"
# print(str.find("Python")) #Found at '0'th index.
# print(str.find("apple")) #-1 as nowhere to be found.


# #index() : Same like find but raises ValueError Excpetion when string not found.
# print(str.index("Python")) #Found at '0'th index.
# print(str.index("apple")) #Throws exception.

#replace() : Replaces a given string with already present string.
# s = "Hello"
# print(s.replace("Hello","Hi")) #Replace Hello -> Hi.
# print(s.replace("Now","Hi")) #Dosnt delete string totally hence returns "Hello".
#If string not present then returns the orignal string without modification.

#split() : In Python, the split() method divides a string into a list of substrings based on a specified delimiter.
# s = "java,c,py,php"
# s1 = s.split(",")
# print(s1)
# s2 = s.split() #Defalut args allowed.
# print(s2)
# s3 = s.split(",",2) #Only splits two elements or 2 times.
# print(s3)
#This always returns strings in list or splitted and stored in list.
# x,y = input("Enter words:").split() #Splits input to x and y.
# print(x," ",y)

