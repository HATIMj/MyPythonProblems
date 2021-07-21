
def dt():
   import datetime                           
   return datetime.datetime.today().year      #using datetime module to get current year
m=input("Do you want to provide us :--Year(y) or Age(a):---[] ")  #Getting input from user if they want to provide their age or birth year
if m=='Age' or m=='a':       #In Age
   n=int(input("Write the age:--"))  #Age input
   if n>125:
      print("you seems to be the oldest person alive")     #if age exceeded 125 then he/she will be oldest person on earth
      exit()   #exiting ...
   elif n<=0:
      print("you are not even born yet")     #opposite condition 
      exit() #exiting....
   
   print(f"You will of 100 years in {dt()+100-int(n)}")  #printing the year when the user's age will be of 100 years
   b=input("Do you want to know your age on any other year y/n:--")       #Age on any other year
   if b=='y':
      c=int(input("Write the year:--"))     
      
      j=int(c)-(dt()-int(n)) 
      print(f"Your age will be {j}")     #Printing the age of user on any given year

   
else:                                      #Here input is taken in years
   n=int(input("Write your birthday year:--"))
   if n<1900 or n>2156:      #Same conditions like above 
      print("you seems to be the oldest person alive")
      exit()    # exiting..... the python file........
   elif n>2021:   #opposite condition 
      print("you are not even born yet")
      exit()# exiting..... the python file........
   print(f"You will be of 100 years on {int(n)+100}") #printing the year when the user's age will be of 100 years
   b=input("Do you want to know your age on any other year y/n:--") #Age on any other year
   if b=='y':
      c=input("Write the year:--")
      j=int(c)-int(n)
      print(f"Your age will be {j}")   #Printing the age of user on any given year
   

   
   




