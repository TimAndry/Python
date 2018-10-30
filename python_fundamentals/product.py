class Store:
  def __init__(self, price, itemName, weight, brand):
    self.itemName = itemName
    self.price = price
    self.weight = weight
    self.brand = brand
    self.status = "for sale"
  def sell(self):
    self.status = "sold"
    return self
  def addTax(self):
    self.tax = 0.1
    self.price = self.price + (self.price *self.tax)
    return self
  def returned(self, reason):
    self.reason = reason
    if self.reason == "defective":
      self.price = 0
    elif self.reason == "like new":
      self.status = "for sale"
      self.price = self.price/(1+self.tax)
    elif self.reason == "opened":
      self.price = self.price/(1+self.tax)
      self.price = self.price - (self.price *.20)
      self.status = "for sale"
    return self
  def displayInfo(self):
    print(self.__dict__)
    return self

item1 = Store(20, "banana", "per/lb", "Chiquita").sell().addTax().returned("opened").displayInfo()