from contact import Contact


class Node:
    def __init__(self, contact):
        self.contact = contact
        self.next = None


class ContactList:

    def __init__(self):
        self.head = None

    def add_contact(self, name, phone):
        contact = Contact(name, phone)

        new_node = Node(contact)

        if not self.head:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def view_contacts(self):
        current = self.head

        while current:
            print(
                f"{current.contact.name} - {current.contact.phone}"
            )
            current = current.next

    def search_contact(self, name):
        current = self.head

        while current:
            if current.contact.name.lower() == name.lower():
                return current.contact

            current = current.next

        return None

    def delete_contact(self, name):

        if not self.head:
            return False

        if self.head.contact.name.lower() == name.lower():
            self.head = self.head.next
            return True

        current = self.head

        while current.next:
            if current.next.contact.name.lower() == name.lower():
                current.next = current.next.next
                return True

            current = current.next

        return False