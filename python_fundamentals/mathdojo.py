class MathDojo:
  def __init__(self):
    self.sumi = 0
  def add(self, *args):
    for i in range(0, len(args)):
      self.sumi = self.sumi + args[i]
    return self
  def subtract(self, *args):
    for i in range(0, len(args)):
      self.sumi = self.sumi - args[i]
    return self
  def printResult(self):
    print(self.sumi)
  
x = MathDojo().add(2).add(2,5,1).subtract(3,2).printResult()