# Task 1
# Write a Program to take input from employee and print
# Employee Name, Salary, Department, Experience.

e_name = input("Enter Employee Name: ")
e_salary = input("Enter Employee Salary: ")
e_dept = input("Enter Employee Department: ")
e_exp = input("Enter Employee Experience: ")

print("Employee Name:", e_name)
print("Employee Salary:", e_salary)
print("Employee Department:", e_dept)
print("Employee Experience:", e_exp)

# Task 2
# Write a program to print product details:
# Product Name, Price, Quantity.

p_name = input("Enter Product Name: ")
p_price = input("Enter Product Price: ")
p_quantity = input("Enter Product Quantity: ")

print("Product Name:", p_name)
print("Product Price:", p_price)
print("Product Quantity:", p_quantity)

# Task 3
# Write a Program Addition of Two Numbers

a = float(input("Enter a number: "))
b = float(input("Enter another number: "))

print("Addition of numbers:", a + b)

# Task 4
# Write a Program to calculate Area of Rectangle
# Formula: width * length

w = float(input("Enter width of rectangle: "))
l = float(input("Enter length of rectangle: "))

print("Area of rectangle:", w * l)

# Task 5
# Write a Program to calculate Simple Interest
# Formula: (P * R * T) / 100

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time: "))

print("Simple Interest:", (p * r * t) / 100)

# Task 6
# Write a Program to take user name and print welcome message.

u_name = input("Enter Name: ")
print("Welcome!", u_name)

# Task 7
# Write a Program to take radius and calculate circle area.

r = float(input("Enter radius: "))
print("Area of circle:", 3.14 * r * r)

# Task 8
# Take marks and print total marks.

English = float(input("Enter marks in English: "))
Maths = float(input("Enter marks in Maths: "))
Science = float(input("Enter marks in Science: "))

print("Marks in English:", English)
print("Marks in Maths:", Maths)
print("Marks in Science:", Science)
print("Total marks:", English + Maths + Science)