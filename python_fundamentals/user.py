# define class User
class User:
    # this method to run every time a new object is instantiated
    def __init__(self, name, email):
	# instance attributes 
        self.name = name
        self.email = email
        self.logged = True
    # login method changes the logged status for a single instance (the instance calling the method)
    def login(self):
        self.logged = True
        print(self.name + " is logged in.")
        return self
    # logout method changes the logged status for a single instance (the instance calling the method)
    def logout(self):
        self.logged = False
        print(self.name + " is not logged in")
        return self
    # print name and email of the calling instance
    def show(self):
        print(f"My name is {self.name}. You can email me at {self.email}.")
        return self



class Bike:
  def __init__(self, price, max_speed):
    self.price = price
    self.max_speed = max_speed
    self.miles = 0
  
  def displayInfo(self):
    self.miles = 0
    print("This bike costs " + self.price + " , and has a max speed of " + self.max_speed + ", and has " + self.miles + " miles on it!" )
    return self

bike1 = Bike(200, "25mph")

displayInfo()