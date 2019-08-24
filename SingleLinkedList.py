from SingleLinkedList1.SingleNode import Node

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.counter = 0

    def insertStart(self, data):
        """insert node at start and it's time complexity is O(1)"""

        self.counter += 1

        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def insertEnd(self, data):
        """insert node at end and it's time complexity is O(n)"""

        self.counter += 1
        #to insert the node at start
        if self.head is None:
            self.insertStart(data)
            return

        newNode = Node(data)
        actualNode = self.head
        #traversing to last node
        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def remove(self, data):

        if self.head:
            if data == self.head.data:#to remove first node
                actualNode = self.head
                self.head = self.head.nextNode
                del actualNode.data
                del actualNode.nextNode
                self.counter -= 1
                print("Node is deleted")
            else:
                check = self.head.remove(data, self.head)#calling node class method and remove node except first
                if (check == -1):
                    self.counter -= 1
                    print("Node is deleted")
                else:
                    print("Data is not present in the list")
        else:
            print("List is empty")

    #to traverse node
    def traverseList(self):

        if self.head:
            actualNode = self.head

            while actualNode is not None:
                print("{}".format(actualNode.data))
                actualNode = actualNode.nextNode
        else:
            print("List is empty")
