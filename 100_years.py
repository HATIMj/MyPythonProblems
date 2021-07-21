
def dt():
   import datetime
   return datetime.datetime.today().year
m=input("Do you want to provide us :--Year(y) or Age(a):---[] ")
if m=='Age' or m=='a':
   n=int(input("Write the age:--"))
   print(f"You will of 100 years in {dt()+100-int(n)}")
   b=input("Do you want to know your age on any other year y/n:--")
   if b=='y':
      c=int(input("Write the year:--"))
      
      j=int(c)-(dt()-int(n))
      print(f"Your age will be {j}")
   if n>125:
      print("you seems to be the oldest person alive")
   elif n<=0:
      print("you are not even born yet")
   else:
      pass
else:
   n=int(input("Write your birthday year:--"))
   
   print(f"You will be of 100 years on {int(n)+100}")
   b=input("Do you want to know your age on any other year y/n:--")
   if b=='y':
      c=input("Write the year:--")
      j=int(c)-int(n)
      print(f"Your age will be {j}")
   if n<1900 or n>2156:
      print("you seems to be the oldest person alive")
   elif n>2021:
         print("you are not even born yet")

   
   




