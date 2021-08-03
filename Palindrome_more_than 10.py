                                              #Palindrome of number more than 10  

n=list(map(int,input("Give some numbers for list separated with space:-- ").split(" "))) #Taking input as list separated by space 
m=[]     #Making a new empty list m

def pal(n):
    """This function returns the next palindrome"""
    n+=1
    while not str(n)==str(n)[::-1]:
        n+=1
    return n
for i in n: #Looping the list elements
    if i>10:   #If any element of list is more than 10. Then its palindrome is printed inside the list
        j=pal(i)  #Putting i in function to scan i and give results
        m.append(j) #Now appending the palindrome elements in new list
    else:
        m.append(i) #Now appending the remaining elements inside the new list
print(m)