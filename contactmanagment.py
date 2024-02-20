class ContactManagementSystem:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email):
        self.contacts[name] = {'phone': phone_number, 'email': email}
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for name, info in self.contacts.items():
                print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

    def edit_contact(self, name, phone_number=None, email=None):
        if name in self.contacts:
            if phone_number:
                self.contacts[name]['phone'] = phone_number
            if email:
                self.contacts[name]['email'] = email
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")


# Example usage:
if __name__ == "__main__":
    cms = ContactManagementSystem()

    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            cms.add_contact(name, phone_number, email)
        elif choice == '2':
            cms.view_contacts()
        elif choice == '3':
            name = input("Enter name of contact to edit: ")
            phone_number = input("Enter new phone number (leave blank to keep existing): ")
            email = input("Enter new email (leave blank to keep existing): ")
            cms.edit_contact(name, phone_number, email)
        elif choice == '4':
            name = input("Enter name of contact to delete: ")
            cms.delete_contact(name)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
