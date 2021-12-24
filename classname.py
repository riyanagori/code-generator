class Car:
    def __init__(self,fuel,price,year):
      self.fuel = fuel
      self.price= price
      self.year = year

    def dat(self):
      print("the fuel is:", self.fuel)
      print("the price is:", self.price)
      
          

c1 = Car("petrol",120000,2020)
c2 = Car("diesel",20000,1999)
c2.dat() 
del c1.year 
del c2.year
print(c1)
print(c2)



 

