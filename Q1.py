class node:
  def __init__(self,A):
    self.A = A;
    self.top = 0;
    self.new_stack = []

class DerivedStack(node):
 def _init__(self,A):
    node.__init__(self,A)
 def push(self,val):
    if(self.top==self.A):
      print("Stack is full ")
    else:
        self.new_stack.append(val)
        print("-- > {} is stored in the stack".format(self.new_stack[self.top]))
    self.top += 1

    def pop(self):
            if(self.top==0):
             print("Stack is empty ")
            else:
              self.top-=1
            print("-- >{} is deleted from the stack".format(self.new_stack[self.top]))
    def display(self):
         for x in range(self.top,0,-1):
            print(" {} \n".format(x))
    def _del__(self):
      print("Calling Destructor")
S= DerivedStack(5)
S.push(1)
S.push(2)
S.push(3)
S.push(4)
S.push(5)
S.display()
S.pop()
S.pop()
S.display()
del S
