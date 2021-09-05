                                                             #Funny name creator by jumbling the last name of the various names


s=int(input("How many names do you need to add:-"))  #Taking the number of names as an input 
k=[]             #Creating a list which will contain these names
for i in range(s):                  #Iterating until the number of names 
    j=input("write the name here:--")    #Taking the names as an input
    l=j.split(" ")           #Splitting it by space
    if len(l)>2:               #If name contains Any Middle name or any other name Then Program will print an error and will exit itself 
        print("Please Don't Enter any Middle Name.Enter only First and Last Name.")
        exit()
    else:k.append(j)       #Else it will append the names in the list

def swapper(k,s):
    '''This Function Takes List of names and Number of names as an arguement and jumble the last names of the names to make them funnier'''
    import random      #Importing Random module
    f=[]                #Creating a list of first names which has a nested list 
    sur=[]              #Creating a list of surnames 
    new=[]              #Creating a new list of jumbled names
    fir=[]              #List which contain first names (removed the nested list from f list)
    def nr(f):  
        '''This function removes the nestedd list inside of the list'''
        for i in f:   #Iterating tothe list
           if type(i)==list:nr(i)   #If any element of list contains a list Then It will call itself again until the nested brackets are removed 
           else:fir.append(i)      #Else it will append it to the fir list
#--------------------------------------------------------------------------------------------------------------------------------------------------------------#
    for i in k:          #Iterating through the list 
       m=i.split(" ")    #Spiltting the elments with space 
       f.append(m[:len(m)-1])   #Appending the First Name which we can also get by writing m[0]  
       sur.append(m[len(m)-1])   #Appending the last Name which we can also get by writing m[1]
    nr(f)          #Due to slicing the f in somewhat complex way it created the nezted lists so now i am removing the list brackets from the elemets 
    for i in range(s):    #Iterating and then appending the n(jumbled name ) to new list
        e=random.choice(sur) 
        n=f" {fir[i]} {e}" 
        new.append(n)
    for i in new:#Iterating through the list to print it
        print(i)
swapper(k,s)              #Calling the function
