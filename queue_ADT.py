from node import Node


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def append(self, item):
        new_node = Node(item, None)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node

    def serve(self, item):
        if self.is_empty():
            raise StopIteration("there is nothing to give you!!")
        item = self.front.item
        self.front = self.front.next
        if self.is_empty():
            self.rear = None
        return item
