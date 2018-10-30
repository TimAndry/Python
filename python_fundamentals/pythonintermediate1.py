def randomInt(mn, mx):
  import random
  if mn > 0 and mx > mn:
    number = mn + random.random()*mx
    print(int(number))
  elif mn > 0:
    mx=100
    number = mn + random.random()*mx
    print(int(number))
  elif mx > 0:
    mn=0
    number = random.random()*mx
    print(int(number))

    


randomInt(0, 3)

def randomProgram():

class User:
    name="Anna"
anna = User()
print("anna's name:", anna.name)                            
User.name = "Bob"
print("anna's name after change:", anna.name)               
bob = User()
print("bob's name:", bob.name)                              
