
import random

otp = random.randint(100000, 999999)

print("OTP Generator")
print("--------------------")
print("Your generated OTP is:", otp)

verify_otp = int(input("Enter the OTP to verify: "))

if verify_otp == otp:
    print("OTP Verified Successfully!")
else:
    print("Invalid OTP!")
