class Stack:
    def __init__(self):
        self.items=[]
    
    def is_empty(self):
        return len(self.items)==0
    
    def push(self,item):
        self.items.append(item)

    def delete(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
        
    def size(self):
        return len(self.items)
    

stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("stack size:",stack.size())
print("pop item:",stack.peek())
print("pop item:",stack.delete())
print("stack size after poping:",stack.size())





    
