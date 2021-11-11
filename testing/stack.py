from testing.node import Node, view






class EmptyStack(Exception) :
    pass




class Stack :    
    def __init__(self) :
        self.top = None

    def push(self,value) : 
        node = Node(value)
        if self.top :
            node.next = self.top
        self.top = node
        
    def pop(self) : 
        try :
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
        except EmptyStack :
            raise EmptyStack('Its Empty')

    def peek(self) : 
        pass

    def isEmpty(self) : 
        pass



if __name__ =="__main__":
    view()
    view()