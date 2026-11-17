# Calculator and Area Calculation

import math

print("----- BASIC CALCULATOR -----")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Cannot divide by zero")

print("\n----- AREA CALCULATION -----")

print("1. Rectangle")
print("2. Square")
print("3. Circle")
print("4. Triangle")

choice = int(input("Enter your choice: "))

if choice == 1:
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    print("Area of Rectangle:", length * breadth)

elif choice == 2:
    side = float(input("Enter side: "))
    print("Area of Square:", side * side)

elif choice == 3:
    radius = float(input("Enter radius: "))
    print("Area of Circle:", math.pi * radius * radius)

elif choice == 4:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Area of Triangle:", 0.5 * base * height)

else:
    print("Invalid choice")