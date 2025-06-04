import pickle
import csv

def save_directory(directory):
    with open('telephone_directory.dat', 'wb') as file:
        pickle.dump(directory, file)

def load_directory():
    try:
        with open('telephone_directory.dat', 'rb') as file:
            directory = pickle.load(file)
    except (FileNotFoundError, EOFError):
        directory = {}
    return directory

def print_banner():
    banner = """
    ***************************************
    *                                     *
    *  TELEPHONE DIRECTORY MANAGEMENT     *
    *              SYSTEM                 *
    *                                     *
    ***************************************
    """
    print(banner)

def add_contact(directory):
    ans = 'y'
    while ans == 'y':
        name = input("Enter the name of the No. Owner: ")
        if name in directory:
            print("Contact already exists. Use update to change the details.")
            return
        phone = int(input("Enter the Telephone No. : "))
        email = input("Enter the Owner's Email: ")
        directory[name] = {"phone": phone, "email": email}
        save_directory(directory)
        print("Contact added successfully!")
        ans = input("Want to enter more records (y,n): ")

def delete_contact(directory):
    name = input("Enter the name of the contact to delete: ")
    if name in directory:
        del directory[name]
        save_directory(directory)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def update_contact(directory):
    name = input("Enter the name of the contact to update: ")
    if name in directory:
        print(f"Current Details - Phone: {directory[name]['phone']}, Email: {directory[name]['email']}")
        directory[name]['phone'] = input("Enter new Phone Number: ")
        option1 = input("Do you want to update the email address? (y/n): ")
        if option1 == 'y':
            directory[name]['email'] = input("Enter new Email Address: ")
        save_directory(directory)
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def search_contact(directory):
    search_type = input("Search by (1) Name, (2) Phone Number, (3) Email: ")
    if search_type == '1':
        name = input("Enter the name to search: ")
        if name in directory:
            print(f"Contact found: Phone: {directory[name]['phone']}, Email: {directory[name]['email']}")
        else:
            print("Contact not found.")
    elif search_type == '2':
        phone = input("Enter the phone number to search: ")
        found = False
        for name, details in directory.items():
            if str(details['phone']) == phone:
                print(f"Contact found: Name: {name}, Email: {details['email']}")
                found = True
                break
        if not found:
            print("Contact not found.")
    elif search_type == '3':
        email = input("Enter the email to search: ")
        found = False
        for name, details in directory.items():
            if details['email'] == email:
                print(f"Contact found: Name: {name}, Phone: {details['phone']}")
                found = True
                break
        if not found:
            print("Contact not found.")
    else:
        print("Invalid choice. Please try again.")

def view_contacts(directory):
    if not directory:
        print("No contacts found.")
    else:
        for name, details in directory.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

def export_to_csv(directory):
    with open('telephone_directory.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email"])
        for name, details in directory.items():
            writer.writerow([name, details['phone'], details['email']])
    print("Contacts exported to telephone_directory.csv successfully!")

def TDMS():
    '''TELEPHONE DIRECTORY MANAGEMENT SYSTEM (TDMS)'''
    directory = load_directory()
    print_banner()

    while True:
        print("\nTelephone Directory Management")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Export Contacts to CSV")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(directory)
        elif choice == '2':
            view_contacts(directory)
        elif choice == '3':
            search_contact(directory)
        elif choice == '4':
            update_contact(directory)
        elif choice == '5':
            delete_contact(directory)
        elif choice == '6':
            export_to_csv(directory)
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

TDMS()
