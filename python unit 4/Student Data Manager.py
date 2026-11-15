


filename = "students.txt"


with open(filename, "a") as file:
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = input("Enter marks: ")

    file.write(f"{roll_no}, {name}, {marks}\n")

print("\nStudent details saved successfully!")


print("\nStudent Records:")

with open(filename, "r") as file:
    for line in file:
        print(line.strip())
