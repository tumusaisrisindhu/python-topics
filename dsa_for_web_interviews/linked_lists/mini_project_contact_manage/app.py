from linked_list import ContactList

contacts = ContactList()

contacts.add_contact("Sai", "9876543210")
contacts.add_contact("Rahul", "9876500000")
contacts.add_contact("Priya", "9123456789")

print("CONTACT LIST")
contacts.view_contacts()

print("\nSEARCHING PRIYA")
found = contacts.search_contact("Priya")

if found:
    print(found.name, found.phone)

print("\nDELETING RAHUL")
contacts.delete_contact("Rahul")

print("\nUPDATED LIST")
contacts.view_contacts()