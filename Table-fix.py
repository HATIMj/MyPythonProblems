                                          #Table Fixer and Breaker Functions
i=int(input("Which multiplication table do you want:--"))   #Taking input
m=[]     #Creating New List
def breaker(n):
    '''This function creates a wrong table'''
    import random      
    
    x=random.randint(1,10)   #Selecting a random number
    for i in range(11):  #Iterating until 10
        m.append(n*i)     #Appending the value to the list
        if i == x:        #If i is equal to any random number then it will multipl it with 11 to create a mistake
            m.remove(i*n)   #It will remove the right value 
            m.append(11*i)    #And will put the wrong value
    print(m)         #Printing the list 
breaker(i)
def fixer(n,m):
    '''This Function fixes the mistakes in table.'''
    for i in m:   #Itertaing through the list 
        if i/n==m.index(i):   #If element of list divided by n(a number on basis of which Table list created) is qual to index of i in m then it will print the value
            print(i)
        else:print(f"value is wrong.\nThe correct value is {n*m.index(i)}.")
         # If not it will print that the value is wrong 
fixer(i,m)

