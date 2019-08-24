
class Node(object):#to create node

    def __init__(self, data):
        self.data = data
        self.nextNode = None

    def remove(self, data, previousNode):

        if self.data == data:
            previousNode.nextNode = self.nextNode
            del self.data
            del self.nextNode
            return -1

        else:
            if self.nextNode is not None:
                return self.nextNode.remove(data, self)#calling recursively and passing refernce of self in order current and previous Node