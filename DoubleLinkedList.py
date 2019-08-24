from DoublyLinkedList1.Node import Node

class DoublyLinkedList(object):

    def __init__(self):
        self.head = None
        self.count = 0

    def get_count(self):
        return self.count

    def insertStart(self, data):#ti insert the node at start
        newNode = Node(data)#creating new node and making a object of it
        self.count += 1

        if not self.head:#if there is no node on start
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head.previousNode = newNode
            self.head = newNode

    def insertEnd(self, data):#to insert the node at end
        self.count += 1
        if not self.head:#if the list is empty
            self.insertStart(data)
        else:
            copyNode = self.head#making a reference copy of first node
            while copyNode.nextNode != None:#reaching at last node
                copyNode = copyNode.nextNode

            newNode = Node(data)
            copyNode.nextNode = newNode
            newNode.previousNode = copyNode

    def insertMid(self, pos, data):#to insert the node in mid posotion
        if(pos == 0):
            self.insertStart(data)
        elif(pos == self.get_count()):
            self.insertEnd(data)
        elif(0<pos<self.get_count()):
            self.count += 1
            necoNode = self.head#making a reference copy of first node

            for i in range(pos):#reaching to that node
                bacoNode = necoNode#track previous node
                necoNode = necoNode.nextNode
            newNode = Node(data)

            bacoNode.nextNode = newNode
            newNode.previousNode = bacoNode

            newNode.nextNode = necoNode
            necoNode.previousNode = newNode
        else:
            print("You have entered wrong index and enter index in [0, {}]".format(self.get_count()))

    def remove(self, data):
        if self.head:
            if data == self.head.data:#to remove first node
                actualNode = self.head
                self.head = self.head.nextNode
                self.previousNode = None
                actualNode.nextNode = None
                del actualNode.data
                del actualNode.nextNode
                del actualNode.previousNode
                self.count -= 1
                print("Node is deleted")
            else:
                check = self.head.remove(data, self.head)#calling node class method remove and remove node except first
                if(check == -1):
                    self.count -= 1
                    print("Node is deleted")
                else:
                    print("Data is not present in the list")
        else:
            print("List is empty")

    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print("{}".format(actualNode.data))
            actualNode = actualNode.nextNode

