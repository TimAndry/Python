class Animal:
  def __init__(self, name, health):
    self.name = name
    self.health = health
  def walk(self):
    self.health = self.health - 1
    return self
  def run(self):
    self.health = self.health - 5
    return self
  def displayHealth(self):
    print(self.health)
    return self
  
class Dog(Animal):
  def __init__(self):
    super().__init__()
    self.health = 150
  def pet(self):
    self.health = self.health + 5

class Dragon(Animal):
  def __init__(self):
    super().__init__()
    self.health = 170
  def fly(self):
    self.health = self.health - 10
  def showHealth(self):
    print("I am a Dragon")
    

animal1 = Animal("one", 100).walk().walk().walk().run().run().displayHealth()
