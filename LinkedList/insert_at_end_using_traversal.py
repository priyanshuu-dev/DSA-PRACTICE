class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

n1.next = n2
n2.next = n3


new = Node(40)

temp = n1

while temp.next:
    temp = temp.next


temp.next = new

temp = n1

while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")