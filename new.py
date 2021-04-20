class MyName():
  def __init__(self):
      self.name=None
    
   def __call__(self, name="someone"):
       self.myname=name
       return "memorized"
     
myam=MyName()
print(myam.("MKD"))
  
  
