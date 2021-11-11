from testing.node import Node, view

class Queue :
    def __init__(self) :
        self.front = None
        self.rear = None
    
    def enqueue(self,value) :
        node = Node(value)
        if not self.rear :
            self.front = node
            self.rear = node
        else :
            self.rear.next = node
            self.rear = node

    def dequeue(self) :
        pass

    def peak(self) :
        pass

    def isEmpty(self) :
        return self.front == None
# Other Way        return self.rear == None








if __name__ =="__main__":
    view()
    view()

