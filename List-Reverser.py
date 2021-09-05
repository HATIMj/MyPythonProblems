                             #List  reverser :- This program reverse a list using inbuilt function , string slicing and using an algorithm
n=list(map(int,input("Enter list of five numbers:").split(" ")))  #Taking the in input for a list separated by " " space
m=n[::-1]   #reversing by string slicing 
j=n[:]     #Now j is the copy of n(input) 
j.reverse()    #reversing j with inbuilt function
print(f"My first reverse of {n} is {j}")     #Printing the statements
print(f"My second reverse of {n} is {m}")
h=n[:]    #h is the copy of n(input)
for i in range(len(h)//2):        #Halfing the loop to get the result
    h[i],h[len(h) -i -1]=h[len(h) -i -1],h[i]   #This algorithm swaps the elemts of the list so that it become reversed
print(f"My third reverse of {n} is {h}")   #printing the statement
if h==j and h==m:print("All lists reversed successfully")  #If the conditions are satisfied it will print this given statement else it will print the oother statement
else:print("Lists are not reversed successfully")





