


num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")




n = int(input("\nEnter a number to find factorial: "))

factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print("Factorial of", n, "is", factorial)
