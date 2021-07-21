n=int(input("Enter your birthyear or age:--")) #Taking the input from user about his age or the birth year

pear=2021 #current year

Aage=False   #initializing.....
Aayear=False  #initializing.....
if (len(str(n)))==4: #if the length of string is 4 then it is the year else it will be age of the user
  Aayear=True    #True if its an year
else:
  Aage=True      #True if input is an age
if n<1900 and Aayear: #if his birth year is less than 1900.Then he or she will be the oldest person alive on this earth
  print("You seems to be the oldest person alive on earth") 
  exit()  #Exiting the program and error occured
elif n>2021 and Aayear:     #if year of birth is more than current year then user is not born 
  print("You are not yet born")
  exit()   #Exiting......
if Aage:    #if the input is an age
  n=2021-n   #Then input will be equal to differnece between the input and the current year which will ultimately equal to Birth Year
print(f"Your age will be of 100 years in {n+100}")  #Printing the year when the user's age will be of 100 years
i=int(input("Enter the year in which you want to know your age:--"))#An another input if user want to know his age on an other year
print(f"Your age in {i} will be {i-n}")#Printing the age of the user on the given year

