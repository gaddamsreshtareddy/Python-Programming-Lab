# Scientific Calculator for Two Numbers

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("\n----- CALCULATOR -----")

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
    print("Floor Division:", num1 // num2)
    print("Modulus:", num1 % num2)
else:
    print("Division: Cannot divide by zero")
    print("Floor Division: Cannot divide by zero")
    print("Modulus: Cannot divide by zero")

print("Exponentiation:", num1 ** num2)