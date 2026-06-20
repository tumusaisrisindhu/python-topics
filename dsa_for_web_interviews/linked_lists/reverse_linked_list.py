class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev

        prev = current
        current = next_node

    return prev


def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print("Original:")
print_list(head)

head = reverse(head)

print("\nReversed:")
print_list(head)