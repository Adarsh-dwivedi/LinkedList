class Node(object):

    def __init__(self, data):
        self.previousNode = None
        self.data = data
        self.nextNode = None

    def remove(self, data, backNode):

        if self.data == data:#to delete second onward node
            backNode.nextNode = self.nextNode#
            self.previousNode = None

            if self.nextNode:#so that the peoblem is not come in deleting last node
                self.nextNode.previousNode = backNode
            self.nextNode = None

            del self.data
            del self.nextNode
            del self.previousNode
            return -1#we can decrement the value of self.count if node is deleted

        else:
            if self.nextNode is not None:
                return self.nextNode.remove(data,self)  # calling recursively and passing refernce of self in order current and previous Node
