# Implementation of stack to be used in the scan algorithm
class Stack:
    def __init__(self):
        self.__items = []
    # add to the top element of the stack
    def push(self, item):
        self.__items.append(item)

    # remove from the top element of the stack
    def pop(self):
        if not self.is_empty():
            return self.__items.pop()

    # to get the top element of the stack
    def peek(self):
        if not self.is_empty():
            return self.__items[-1]
        return None

    # to check if the stack is empty
    def is_empty(self):
        return len(self.__items) == 0

    # size of stack
    def size(self):
        return len(self.__items)