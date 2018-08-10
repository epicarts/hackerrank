# linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def insert(self,head,data):
    #Complete this method
        self.data = data
        if head is None:
            return Node(self.data)
        else:
            current = head
            while(True):
                if current.next is None:
                    new_node = Node(self.data)
                    current.next = new_node
                    return head
                current = current.next


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);
