class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None

    def remove(self, data, previousNode, obj):

        if self.data == data:
            #to update the last node
            if obj.lastNode is self:
                obj.lastNode = previousNode

            previousNode.nextNode = self.nextNode
            del self.data
            del self.nextNode
            return -1

        else:
            if self.nextNode is not None:
                return self.nextNode.remove(data, self, obj)  #calling recursively and passing refernce of self in order current and previous Node
