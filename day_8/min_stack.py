##### Min Stack ####

class MinStack:
    def __init__(self):
        self.stack=[]
        self.minStack=[]
    
    def push(self,val):
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))
    
    def pop(self):
        self.stack.pop()
        self.minStack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minStack[-1]

array = [3,2,5,7,1,2,9]
stack1=MinStack()
stack2=MinStack()

for i in array:
    stack1.push(i)

print(stack1.top(),stack1.getMin())
    