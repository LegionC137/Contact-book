contacts = {}

def add_contact():
    name = input(" name: ").strip()
    phone = input(" phone: ").strip()

    if not name or not phone:
        print("  name and phone cannot be empty")
        return

    contacts[name] = phone
    print(f" contact {name} = {phone}")

def search_contact():
    name = input("search name: ").strip()
    if not name:
        print("  name cannot be empty")
        return

    phone = contacts.get(name)
    if phone:
        print(f" found: {name} = {phone}")
    else:
        print(f" contact not found")

def update_contact():
  name = input("Name to update: ").strip()
  if name not in contacts:
      print("Contact not found")
      return
  new_phone = input("New phone number: ").strip()
  if not new_phone:
      print("Phone number cannot be empty")
      return
  contacts[name] = new_phone
  print(f" contact {name} updated to {new_phone}")

def view_all():
   if not contacts:
      print(" no contacts")
      return

print(" ---contacts---")
for name, phone in contacts.items():
   print(f" {name}  {phone}")

def menu():
   print("\n--- Contact Book ---") 
   print("1. Add Contact")
   print("2. Search Contact")
   print("3. Update Contact")
   print("4. View All ")
   print("5. Exit")
 
def main():
    while True:
        menu()
        choice = input("choose option: ").strip()
        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            view_all()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print(" Please choose 1,2,3,4 or 5.")

if __name__ == "__main__":
    main()
 
