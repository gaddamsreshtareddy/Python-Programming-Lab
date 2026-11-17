# Retail Sales Dashboard

import csv
import matplotlib.pyplot as plt

sales = [
    ["Product", "Sales"],
    ["Laptop", 50000],
    ["Mobile", 30000],
    ["Tablet", 20000],
    ["Headphones", 10000]
]

with open("sales.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(sales)

products = []
amounts = []

with open("sales.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        products.append(row["Product"])
        amounts.append(int(row["Sales"]))

print("----- RETAIL SALES REPORT -----")

for i in range(len(products)):
    print(products[i], ":", amounts[i])

print("Total Sales:", sum(amounts))

plt.bar(products, amounts)
plt.title("Retail Sales Dashboard")
plt.xlabel("Products")
plt.ylabel("Sales Amount")
plt.show()