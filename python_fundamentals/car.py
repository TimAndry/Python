class Car:
  def __init__(self, price, speed, fuel, mileage):
    self.price = price
    self.speed = speed
    self.fuel = fuel
    self.mileage = mileage
    self.tax = .12
  def displayAll(self):
    if self.price > 10000:
      self.tax = 0.15
      #self.price = self.price + (self.price * self.tax)
    #elif self.price < 10000:
      #self.price = self.price + (self.price * self.tax)
    print(self.__dict__)
    return self

car1 = Car(2000, "35mph", "full", "15mpg").displayAll()

car1 = Car(2000, "5mph", "not full", "105mpg").displayAll()

car1 = Car(2000, "15mph", "kind of full", "95mpg").displayAll()

car1 = Car(2000, "25mph", "full", "25mpg").displayAll()

car1 = Car(2000, "45mph", "empty", "25mpg").displayAll()

car1 = Car(2000000, "35mph", "full", "15mpg").displayAll()   