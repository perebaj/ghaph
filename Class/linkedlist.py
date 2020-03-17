from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
    
    def adiciona_Elemento(self, element):
        if self.head:
            pointer = self.head 
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(element)
        else:
            self.head = Node(element)
        self._size += 1

    def __len__(self):
        print(self._size)

    def __getitem__(self, index):
        pointer = self.head
        for _ in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            print(pointer.data)
        else:
            raise IndexError("List index out of range")
    
    def __setitem(self, index, element):
        pointer = self.head
        for _ in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            pointer.data = element
        else:
            raise IndexError("List index out of range")

    def index(self, element):
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == element:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError("{} is not in list".format(element))


