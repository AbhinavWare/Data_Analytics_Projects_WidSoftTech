#Loop tasks.
#Task 1: Print all even numbers between 1 and 50.
for i in range(1,50):
    if i%2==0:
        print(f"{i} is even!")


#Task 2: Print cube of numbers from 1 to 10.
for i in range(1,11):
    print(f"Cube of {i} is {i*i*i}")

#Task 3: Print multiplication tables from 1 to 10.
for i in range(1,11):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
        
#Task 4: Calculate sum of numbers from 1 to 100.
sum = 0
for i in range(1,101):
    sum+=i
    print(i," sums to ",sum)
    
#Task 5: Calculate product of numbers from 1 to 10.
product = 0
for i in range(1,11):
    product*=i
    print(i," products to ",product)
    
    
#Task 6: Print prime numbers from 1 to 100.
for i in range(2,101):
    prime = True
    
    for j in range(2,i):
       if i%j==0:
        prime = False
        break
    
    if prime:
        print(f"{i} is prime!")


#Task 7: Generate Fibonacci series.
n = int(input("Enter n to find Fibonacci series till it:"))
a = 0
b = 1 #First two digits.
for i in range(n):
    print(a,end=" ")
    a=b
    b=a+b
print()


#Task 8: Print this pattern:
# *
# **
# ***
# ****
# ***** .
for i in range(1,6):
    print("*"* i)
    
    
#Task 13 with 9 & 12: Diamond Pattern. 
#Task 9: Create pyramid star pattern.
for i in range(1,5):
    print(" " *(4-i)+"*"*(2*i-1))
#Task 12: Create reverse pyramid.
for i in range(5,0,-1):
    print(" " *(4-i)+"*"*(2*i-1))


#Task 10: Find average of list elements.
num = [1,2,3,4,5]
sum = 0
i = 0
while i < len(num):
    sum += num[i]
    i+=1
avg = sum / len(num)
print("Average of list:",avg)


#Task 11: Print Armstrong numbers.
num = int(input("Enter number:"))

length = len(str(num))
temp = num
sum = 0
while temp > 0:
    digit  = temp % 10
    sum += digit ** length
    temp = temp // 10
    
if sum == num:
    print(f"{num} is Armstrong number!")
else:
    print(f"{num} is not Armstrong number!")
     





