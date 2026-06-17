#Conditional Statements Task

#Task 1: Check whether number is positive or negative.
num=int(input("Enter any number:"))
if num >= 0:
    print(f"{num} is positive!")
else:
    print(f"{num} is negative!")
    
    
#Task 2: Check whether number is even or odd.
num=int(input("Enter any number:"))
if num%2==0:
    print(f"{num} is even!")
else:
    print(f"{num} is odd!")
    
    
#Task 3: Find largest of two numbers.
num1=int(input("Enter any number:"))
num2=int(input("Enter any number:"))
if num1>num2:
    print(f"{num1} is largest!")
else:
    print(f"{num2} is largest!")
    
    
#Task 4: Find largest of three numbers.
num1=int(input("Enter any number:"))
num2=int(input("Enter any number:"))
num3=int(input("Enter any number:"))
if num1>num2 and num1>num3:
    print(f"{num1} is largest!")
elif num2>num1 and num2>num3:
    print(f"{num2} is largest!")
else:
    print(f"{num3} is largest!")
    
#Task 5: Grade calculator using marks.
#We will consider marks in English, Maths, and Science and based on their avergae calculate grade.
English=float(input("Enter marks in English:"))
Maths=float(input("Enter marks in Maths:"))
Science=float(input("Enter marks in Science:"))

mark_avg=(English+Maths+Science)/3
match mark_avg:
    case mark_avg if mark_avg > 90:
        print(f"{mark_avg} gets 'A' grade!")
    case mark_avg if mark_avg > 80 and mark_avg<90:
        print(f"{mark_avg} gets 'B' grade!")
    case mark_avg if mark_avg > 70 and mark_avg<80:
        print(f"{mark_avg} gets 'C' grade!")
    case mark_avg if mark_avg > 60 and mark_avg<70:
        print(f"{mark_avg} gets 'D' grade!")
    case mark_avg if mark_avg < 60:
        print(f"{mark_avg} gets 'E' grade!")
    case _:
        print(f"{mark_avg} is a 'F' grade!")
        
        
#Task 6: Login system.
users = {
    "admin": "1234",
    "Abhinav": "ask"
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login Successful")
else:
    print("Login Failed")
    
    
#Task 7: ATM withdrawal system.
#We can integrate above login system here also.
#We consider here after login logic.
balance = float(input("Enter balance:")) #for accurate info or else we have to connect database.
amt_withdraw=float(input("Enter amount withdraw:"))
if amt_withdraw<=balance:
    print(f"{amt_withdraw} : amount successfully withdrawn!")
    print(f"Current amount:{balance-amt_withdraw} is left in balance.")
else:
    print("Insufficient balance!")


#Task 8: Student scholarship eligibility system.
#We consider students attendence and average of assignments and test result.
name=input("Enter name of student:")
attendence = int(input("Enter student attendence percentage:"))
test_result=float(input("Enter test result of student:"))
assignment= float(input("Enter assignment result:"))

average = (test_result+assignment)/2

if attendence >=75 and average >=75:
    print(f"{name} is eligible student for scholarship!")
else:
    print(f"{name} is not eligible student for scholarship!")


#Task 9: Income Tax Calculator. 
income = float(input("Enter annual income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = 12500 + (income - 500000) * 0.20
else:
    tax = 112500 + (income - 1000000) * 0.30

print("Total Tax =", tax)