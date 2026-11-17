# Student Data Manager Using Files

file = "students.txt"

n = int(input("Enter number of students: "))

with open(file, "a") as f:
    for i in range(n):
        name = input("Enter student name: ")
        marks = input("Enter marks: ")

        f.write(name + "," + marks + "\n")

print("\n----- STUDENT RECORDS -----")

with open(file, "r") as f:
    for line in f:
        print(line.strip())