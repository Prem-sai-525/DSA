#Linked List
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    #Print all the elements
    def print_elements(self):
        if self.head is None:
            print("empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,end="->")
                n=n.ref
    #inserting elements
    #add_at_begining
    def add_at_begining(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    #add_at_end
    def add_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            new_node.ref=self.head
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            new_node.ref=n.ref
            n.ref=new_node
    #add_elements_in_between
    #add_before
    def add_before(self,data,x):
        if self.head is None:
            print("The list is empty")
        elif x==self.head.data:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
        else:
            new_node=Node(data)
            n=self.head
            while n.ref.data is not None:
                if x==n.ref.data:
                    break
                n.ref=n.ref.data
            new_node.ref=n.ref
            n.ref=new_node
    #add_after
    def add_after(self,data,x):
        if self.head is None:
            print("The list is empty")
        else:
            new_node=Node(data)
            n=self.head
        while n.ref is not None:
            if x==n.data:
                break
            n=n.ref
        new_node.ref=n.ref
        n.ref=new_node
    #deleting elements
    #delete_at_begining
    def delete_at_begining(self):
        self.head=self.head.ref
    #delete_at_end
    def delete_at_end(self):
        n=self.head
        while n.ref.ref is not None:
            n=n.ref
        n.ref=None
    #delete_by_value
    def delete_by_value(self,x):
        if self.head is None:
            print("The Linked list is empty")
        elif x==self.head.data:
            self.head=self.head.ref
        else:
            n=self.head
            while n.ref is not None:
                if x==n.ref.data:
                    break
                n=n.ref
            n.ref=n.ref.ref
                    

ll=LinkedList()
ll.add_at_begining(30)
ll.print_elements()
print("\n")
ll.add_at_end(40)
ll.print_elements()
print("\n")
ll.add_before(25,40)
ll.print_elements()
print("\n")
ll.add_before(35,25)
ll.print_elements()
print("\n")
ll.add_after(39,25)
ll.print_elements()
print("\n")
ll.add_before(60,30)
ll.print_elements()
print("\n")
ll.add_after(70,60)
ll.print_elements()
print("\n")
ll.delete_at_begining()
ll.print_elements()
print("\n")
ll.delete_at_end()
ll.print_elements()
print("\n")
ll.delete_by_value(70)
ll.print_elements()
print("\n")
ll.delete_by_value(35)
ll.print_elements()
