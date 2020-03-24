#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Lista Ligada:
#          _________    _________     _________     _________
# head --> | 2 | --|--> | 1 | --|-->  | 5 | --|-->  | 3 | --|--> None
#          ---------    ---------     ---------     ---------

from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def adiciona_Elemento_Inicio(self, element):
        new_Node = Node(element)
        new_Node.next = self.head
        self.head = new_Node
        self._size +=1
        
    def adiciona_Elemento(self, element):
        #adiciona um elemento ao final da lista
        if self.head:
            pointer = self.head 
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(element)
        else:
            self.head = Node(element)
        self._size += 1

    def getnode(self, index):
        pointer = self.head
        for _ in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer

    def len(self):
        return self._size

    def __getitem__(self, index):
        pointer = self.getnode(index)
        if pointer:
            print(pointer.data)
        else:
            raise IndexError("List index out of range")
    
    def __setitem__(self, index, element):
        pointer = self.getnode(index)
        if pointer:
            pointer.data = element
        else:
            raise IndexError("List index out of range")

    def index(self, element):
        #Retorna o índice do elemento na lista
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == element:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError("{} is not in list".format(element))

    def insert(self, index, elemento):
        #insere um novo elemento em um determinado index da lista
        node = Node(elemento)
        if index == 0:
            #inserção no começo da lista
            node.next = self.head
            self.head = node
        else:
            pointer = self.getnode(index - 1)
            node.next = pointer.next
            pointer.next = node
        self._size += 1

    def show(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        return r
    def __str__(self):
        return self.show()
    




