# OTP Generator

import random

otp = random.randint(100000, 999999)

print("OTP GENERATOR")
print("Your OTP is:", otp)

user_otp = int(input("Enter the OTP: "))

if user_otp == otp:
    print("OTP verified successfully!")
else:
    print("Invalid OTP!")