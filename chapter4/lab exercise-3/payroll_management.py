# CSV Based Payroll Management System

import csv

file = "payroll.csv"

n = int(input("Enter number of employees: "))

with open(file, "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["Name", "Basic Salary", "Bonus", "Total Salary"])

    for i in range(n):
        name = input("Enter employee name: ")
        salary = float(input("Enter basic salary: "))
        bonus = float(input("Enter bonus: "))

        total = salary + bonus

        writer.writerow([name, salary, bonus, total])

print("\n----- PAYROLL REPORT -----")

with open(file, "r") as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)