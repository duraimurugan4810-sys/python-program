# Unit Converter

print("UNIT CONVERTER")
print("1. Kilometers to Meters")
print("2. Meters to Kilometers")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")
print("5. Kilograms to Grams")
print("6. Grams to Kilograms")

choice = int(input("Enter your choice: "))
value = float(input("Enter the value: "))

if choice == 1:
    result = value * 1000
    print("Result:", result, "meters")

elif choice == 2:
    result = value / 1000
    print("Result:", result, "kilometers")

elif choice == 3:
    result = (value * 9 / 5) + 32
    print("Result:", result, "°F")

elif choice == 4:
    result = (value - 32) * 5 / 9
    print("Result:", result, "°C")

elif choice == 5:
    result = value * 1000
    print("Result:", result, "grams")

elif choice == 6:
    result = value / 1000
    print("Result:", result, "kilograms")

else:
    print("Invalid choice")