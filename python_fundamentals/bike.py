class Bike:
  def __init__(self, price, max_speed):
    self.price = price
    self.max_speed = max_speed
    self.miles = 0

  def displayInfo(self):
    print("This bike costs", self.price , ", has a max speed of" ,self.max_speed, ", and has been ridden for" , self.miles, "miles!" )
    return self

  def ride(self):
    self.miles = self.miles + 10
    print("...Riding")
    return self

  def reverse(self):
    if self.miles >= 5:
      self.miles = self.miles - 5
    print("...Reversing")
    return self

bike1 = Bike("$200", "25mph").displayInfo().ride().ride().ride().reverse().displayInfo()

bike2 = Bike("200", "25mph").displayInfo().ride().ride().reverse().reverse().displayInfo()

bike3 = Bike("200", "25mph").displayInfo().reverse().reverse().reverse().displayInfo()
    