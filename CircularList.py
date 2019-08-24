from CircularLinkedList1.CicularNode import Node

class CircularLinkedList(object):

    def __init__(self):
        self.head = None
        self.count = 0
        self.lastNode = None  #track last node

    def insertStart(self, data):

        self.count += 1
        newNode = Node(data)
        if not self.head:  #if list is empty
            self.head = newNode
            newNode.nextNode = self.head
            self.lastNode = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
            self.lastNode.nextNode = self.head  #updating last node

    def insertEnd(self, data):

        self.count += 1
        newNode = Node(data)
        if not self.head:
            self.insertStart(data)
        else:
            newNode.nextNode = self.lastNode.nextNode
            self.lastNode.nextNode = newNode
            self.lastNode = newNode

    def insertMid(self, pos, data):

            if pos == 0:
                self.insertStart(data)
            elif pos == self.count:
                self.insertEnd(data)
            elif 0<pos<self.count:
                self.count += 1
                copyNode = self.head  # making a reference copy of first node

                for i in range(pos-1):  # reaching to the previous node with pos-1
                    copyNode = copyNode.nextNode
                newNode = Node(data)

                newNode.nextNode = copyNode.nextNode
                copyNode.nextNode = newNode
            else:
                print("You have entered wrong index and enter index in [0, {}]".format(self.count))

    def remove(self, data):

        if self.head:
            if data == self.head.data:  #to remove first node
                actualNode = self.head
                self.head = self.head.nextNode
                self.lastNode.nextNode = self.head  #updating last node
                del actualNode.data
                del actualNode.nextNode
                self.count -= 1
                print("Node is deleted")
            else:
                #passing the reference of cirular list object so that we can update the last node
                check = self.head.remove(data, self.head, self)#calling node class method and remove node except first
                if (check == -1):
                    self.count -= 1
                    print("Node is deleted")
                else:
                    print("Data is not present in the list")
        else:
            print("List is empty")

    def traverseList(self):

        if self.head:
            actualNode = self.head

            print("{}".format(actualNode.data))
            actualNode = actualNode.nextNode

            while actualNode != self.lastNode.nextNode:
                print("{}".format(actualNode.data))
                actualNode = actualNode.nextNode
        else:
            print("List is empty")


