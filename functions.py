"""
You can think of functions like a bunch of code that is intended to do a particular task in the whole Python script. Python used the keyword ‘def’ to define a function.

# Functions
def hello():
  print("Hello")
  print("Hello Again")

# Calling function
hello()

"""

"""
Now as we know any program starts from a ‘main’ function…lets create a main function like in many other programming languages.
"""

def getInteger():
  result = int(input("Enter integer: "))
  return result

def Main():
  print("Started")

  # calling the getInteger function and  
  # storing its returned value in the output variable 
  output = getInteger()      
  print(output)

# now we are required to tell Python  
# for 'Main' function existence 
if __name__=="__main__": 
  Main() 