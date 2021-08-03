                                     #     PALINDROME                PART 2
def pal(n):           
    """Function which gives out the next palindrome"""
    n+=1   #initializing...
    while not ispal(n):   
        n+=1              #if not palindrome then returns next value until we get a palindrome
    return n
def ispal(n): 
    """Function which verfies if the number is a palindrome or not."""
    return str(n)==str(n)[::-1]
if __name__=='__main__':
   n=int(input("Enter the number of test cases:-- "))     #Taking n as input

   num=[]              #Making a new list

   for i in range(n):    #Looping till the total number of  cases completed.
       j=int(input("Give a number whom you want to get next palindrome of:-- "))      
       num.append(j)    #Appending it into new list
   for i in range(n): #Again Looping
       print(f"the next palindrome of {num[i]} is {pal(num[i])}")  #Printing the next palindrome of every element of the list
