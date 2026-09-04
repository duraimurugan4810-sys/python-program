# Program to demonstrate variables, operators and input/output

name = input("Enter your name: ")
age = int(input("Enter your age: "))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\n--- Student Details ---")
print("Name:", name)
print("Age:", age)

print("\n--- Arithmetic Operations ---")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
    print("Modulus:", a % b)
else:
    print("Division: Cannot divide by zero")
    print("Modulus: Cannot divide by zero")

print("\n--- Comparison ---")
print("a is greater than b:", a > b)
print("a is equal to b:", a == b)
print("a is less than b:", a < b)