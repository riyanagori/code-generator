
try:
  print(x)
except NameError:
  print("name error occured")
except:
  print("name error")  
finally:
  print("solved")