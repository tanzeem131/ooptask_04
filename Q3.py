from numpy import *
class node:
       def __init__(self,A):
            self.front = 0
            self.rear = 0
            self.A = A
            self.queue = []
            def enqueue(self,val):
              if(self.rear==(self.A)):
                 print("Queue is full")
              else:
               self.queue.append(val)
              print("--- >f is stored in the queue ",format(self.queue[self.rear]))
            self.rear+=1
            def dequeue(self):
              if(self.rear==self.front):
                 print("Queue is empty")
              else:
                print("--- >{} is deleted from the queue ".format(self.queue[self.front]))
            self.front+=1
            def dispaly(self):
             for x in range((self.front+1),self.rear+1):
                print("{} \n".format(x))
                def _del__(self):
                  print("Calling Destructor")
Q = node(4)
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)
Q.display()
Q.dequeue()
Q.dequeue()
Q.dispaly()
del Q
