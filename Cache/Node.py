# encoding=utf-8
__author__ = 'Hinsteny'

class Node(object):

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        # Number of nodes in list
        self.count = 0

    def add_node(self, cls, data):
        '''
        Add node instance of class cls.
        :param cls:
        :param data:
        :return:
        '''
        return self.insert_node(cls, data, self.tail, None)

    def insert_node(self, cls, data, prev, next):
        '''
        Insert node instaance of class cls.
        :param cls:
        :param data:
        :param pre:
        :param next:
        :return:
        '''
        node = cls(data)
        node.prev = prev
        node.next = next
        if prev:
            prev.next = node
        if next:
            next.prev = node
        if not self.head or next is self.head:
            self.head = node
        if not self.tail or next is self.tail:
            self.tail = node
        self.count += 1
        return node

    def remove_node(self, node):
        if node is self.tail:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        if node is self.head:
            self.head = node.next
        else:
            node.prev.next = node.next
        self.count -= 1

    def get_nodes_data(self):
        '''

        :return:
        '''
        data = []
        node = self.head
        while node:
            data.append(node.data)
            node = node.next
        return node

class FreqNode(DoublyLinkedList, Node):
    '''
    Frequency node containin
    '''