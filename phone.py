import os
os.system("cls")
import json

def search(name):
    with open("contacts.json") as file:
        contacts = json.load(file)
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"{contact['name']}: {contact['phone']}")
            break
    else:
        print("Kontant topilmadi.")


def add():
    with open("contacts.json") as file:
        contacts = json.load(file)

    new = {
        "name": input("Name: "),
        "phone": input("Phone: ")
    }
    contacts.append(new)
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)
        print("Qo'shildi.")


while True:
    print("Kontaktlar dasturi")
    choice = int(input("1. Qidirish 2. Qo'shish 3. Chiqish\n>>> "))
    if choice == 1:
        name = input("Name: ")
        search(name)
    elif choice == 2:
        add()
    else:
        print("Xayr!")
        break
