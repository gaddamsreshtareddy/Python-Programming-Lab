# Frequency Counter Using Dictionary

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] = frequency[num] + 1
    else:
        frequency[num] = 1

print("----- FREQUENCY COUNTER -----")

for num, count in frequency.items():
    print(num, "appears", count, "times")