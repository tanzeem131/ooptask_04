class rectangle:
   def __init__(self,length,breadth):
           self.length= length
           self.breadth= breadth

           def Area(self):
               print("Area of rectangle(R) is {}".format(self.length * self.breadth))

               def Perimeter(self):
                   print("Perimeter of rectangle(R) is {}".format(2 * (self.length + self.breadth)))

               def __del__(self):
                   print("Calling Destructor")

R = rectangle(4,6)
R.Area()
R.Perimeter()
del R