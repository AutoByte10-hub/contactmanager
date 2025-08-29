contacts = []  # tady se budou ukládat kontakty jako slovníky

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts.append({"name": name, "phone": phone})
    print(f"Contact {name} added.")

def view_contacts():
    if not contacts:
        print("No contacts yet.")
    else:
        for c in contacts:
            print(f"{c['name']} - {c['phone']}")

def delete_contact():  
    name = input("Enter the name to delete: ")
    for c in contacts:
        if c['name'] == name:
            contacts.remove(c)
            print(f"Contact {name} deleted.")
            return
    print("Contact not found.")

def edit_contact():
    name = input("Enter the name to edit: ")
    for c in contacts:
        if c['name'] == name:
            new_name = input("Enter new name (leave blank to keep the same): ")
            new_phone = input("Enter new phone number (leave blank to keep the same): ")

            if new_name:
                c['name'] = new_name
            if new_phone:
                c['phone'] = new_phone

            print("Contact updated.")
            return
    print("Contact not found.")

def menu():
    while True:
        print("\n1 = Add contact")
        print("2 = View contacts")
        print("3 = Delete contact")
        print("4 = Edit contact")
        print("5 = Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            edit_contact()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

menu()