class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

ls = [3,5,6,7]

dummy = Node()
current = dummy

for number in ls:
    current.next = Node(number)
    current = current.next

print(current)