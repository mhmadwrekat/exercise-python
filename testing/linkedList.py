"""
Linked List
"""
def view():
    print('\n|------------------------------------------|')
def view2():
    print('\n--------------------------------')
class Node :
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return f'{self.value}'

class LinkedList :
    def __init__(self):
        self.head = None

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else :
            current = self.head
            while current.next != None :
                current = current.next
            current.next = node
        
    def __str__(self):
        output = 'head -> '
        if self.head is None :
            output += None
        else :
            current = self.head
            while(current):
                output += f'{current.value} -> '
                current = current.next
            output += 'None'
            return output

    def zipLists(self, listOne , listTwo):
        finalList = LinkedList()
        currentOne = listOne.head
        currentTwo = listTwo.head
        while currentOne and currentTwo :
            finalList.append(currentOne)
            finalList.append(currentTwo)
            currentOne = currentOne.next
            currentTwo = currentTwo.next
        while currentOne :
            finalList.append(currentOne)
            currentOne = currentOne.next
        while currentTwo :
            finalList.append(currentTwo)
            currentTwo = currentTwo.next
        return finalList

    def insert(self,value):
        node = Node(value)
        if self.head is not None:
            node.next = self.head ## (self.head) The old one
        self.head = node ## (self.head) the new one

    def insert_before(self,value, newValue , list):
        if self.head.value == value:
            list.insert(newValue)
            return list
        current =self.head
        while current is not None:
            print(current.value)
            if current.next.value == value:
                print('yes')
                node = Node(newValue)
                node.next = current.next
                current.next = node
                return list
            current = current.next

    def reverseList(self,listOne):
        newList = LinkedList()
        newList.insert(listOne.head)
        currentOne = listOne.head
        currentOne = currentOne.next
        condition = True
        while condition :
            newList.insert_before(newList.head.value,currentOne,newList)
            currentOne = currentOne.next
            if currentOne.next == None :
                newList.insert_before(newList.head.value,currentOne,newList)
                condition = False
        return newList

listOne = LinkedList()
listOne.append(1)
listOne.append(2)
listOne.append(3)
listTwo = LinkedList()
listTwo.append(5)
listTwo.append(9)
listTwo.append(4)

if __name__ =="__main__":
    ll = LinkedList()
    view()
    print('\nList One :')
    print(listOne)
    print('\nList Two :')
    print(listTwo)
    print('\nZip List One And Two :')
    print(ll.zipLists(listOne,listTwo))
    view2()
    view2()
    print('\nList One :')
    print(listOne)
    view2()
    print('\nReverse List :')
    print(listOne.reverseList(listOne))
    view()
"""
End Linked List
"""