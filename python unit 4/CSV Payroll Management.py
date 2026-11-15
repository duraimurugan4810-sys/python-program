
import csv

filename = "payroll.csv"


name = input("Enter employee name: ")
employee_id = input("Enter employee ID: ")
basic_salary = float(input("Enter basic salary: "))


hra = basic_salary * 0.20
da = basic_salary * 0.10
gross_salary = basic_salary + hra + da


with open(filename, "a", newline="") as file:
    writer = csv.writer(file)

    if file.tell() == 0:
        writer.writerow(["Employee ID", "Name", "Basic Salary",
                         "HRA", "DA", "Gross Salary"])

    writer.writerow([employee_id, name, basic_salary,
                     hra, da, gross_salary])

print("\nPayroll Details Saved Successfully!")


print("\nEmployee Payroll Records:")

with open(filename, "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(" | ".join(row))
