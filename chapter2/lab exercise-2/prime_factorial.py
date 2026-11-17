# Prime Number and Factorial

num = int(input("Enter a number: "))

# Prime Number Check
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# Factorial
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial:", fact)