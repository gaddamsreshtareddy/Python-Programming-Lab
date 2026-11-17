# Contact Book Using Lists and Dictionaries

contacts = []

n = int(input("How many contacts do you want to add? "))

for i in range(n):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    contact = {
        "name": name,
        "phone": phone
    }

    contacts.append(contact)

print("\n----- CONTACT BOOK -----")

for contact in contacts:
    print("Name:", contact["name"])
    print("Phone:", contact["phone"])