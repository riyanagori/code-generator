
login = {"riya":"wwyr56" , "shama":"45gy6o" ,  "shreya":"56rtjj"} 

Finish=False
while not Finish:
  username=input("enter the username:")
  password=input("enter the password:")
  if username==login and password==password:
      continue
  elif password != login[username]:
    print("password is not valid")
    continue
  elif password==login[username]:
    print("welcome",username)
    Finish=True
   
        
    











