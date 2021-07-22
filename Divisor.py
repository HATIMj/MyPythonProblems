                                                 #DIVISOR OR NOT

try:            #trying the below inputs

   n=int(input("Enter the total number of apples:--"))#Taking an input of number of apples 
   mn=int(input("Enter the minimum no. of students:--"))   #Taking the input of minimum number of students
   mx=int(input("Enter the maximum no. of students:--"))    #Taking the input of maximumn number of students
except ValueError:     # if there is no integer in an input it will print the below message and exit the program
    print("Please Enter only integers")
    exit()
if mn==mx:
    if n%mn==0:print(f"This is not a range. {mn} is a divisor of {n}")               #If mn>=mx then it is not a range 
    else:print(f"This is not a range. {mn} is not  a divisor of {n}")  
elif mn>mx:
    print("This is not a range.")
else:
   for i in range(mn,mx+1):   #Looping in range 
       if n%i==0:print(f"{i} is a divisor of {n}")    #Condition to check if it is a divisor
       elif n%i!=0:print(f"{i} is not a divisor of {n}")  #Condition to check if it is not a divisor
       else:pass   #else pass
