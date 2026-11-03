#data types
# sudent information
name = input("Enter name: ")
age = int(input("Enter age: "))
branch = input("Enter branch: ")
cgpa = float(input("Enter CGPA: "))

print(f"My name is {name}, age is {age},branch is {branch} and CGPA is {cgpa}.")

# Swapping two numbers
a = int(input("Enter a: "))
b = int(input("Enter b: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

# simple interest calculation
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

si = (p * r * t) / 100

print("Simple Interest:", si)

#convert data types
a = "100"

b = int(a)
c = float(a)

print(b, type(b))
print(c, type(c))

# conditional statements
# even or odd
num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

#largest of three numbers
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a >= b and a >= c:
    print("A is largest")
elif b >= a and b >= c:
    print("B is largest")
else:
    print("C is largest")

# leap year
year = int(input("Enter year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")

#atm Withdrawal
balance = 10000

amount = int(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Invalid Amount")
elif amount <= balance:
    balance = balance - amount
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance")

# loops
#multiplication table
num = int(input("Enter number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

#sum of natural numbers
n = int(input("Enter number: "))
total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum:", total)

#Factorial of a Number
n = int(input("Enter number: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial:", fact)

#Reverse a Number
num = int(input("Enter number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse:", reverse)

#Functions
#Addition Function
def add(a, b):
    return a + b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

result = add(x, y)
print("Addition:", result)

#Even or Odd Function
def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter number: "))
print(check(n))

#Prime Number Function
def prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

num = int(input("Enter number: "))

if prime(num):
    print("Prime Number")
else:
    print("Not a Prime Number")

#Palindrome Function
def palindrome(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    if original == reverse:
        return "Palindrome"
    else:
        return "Not Palindrome"

num = int(input("Enter number: "))
print(palindrome(num))