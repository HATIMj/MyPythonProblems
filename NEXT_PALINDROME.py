                                                                        #NEXT PALINDROME
j=int(input("Enter the number of test cases:--"))#Taking the input of number of test cases

def m(n):
   """This function reverse the given number"""
   rev_n=0       #LOGIC
   while n!=0:
      rem=n%10
      rev_n=(rev_n*10) + rem
      n=n//10
   return rev_n
def jojo(): 
   """This function scan all the next numbers of the given number to get a palindrome and stop when the mission is completed"""
   for i in range(l+1,l*10): #Looping from next l+1 to l*10 so that it can get palindrome without any error
       if i==m(i):
          return "{} is the next palindrome".format(i)
          break
       else:

          pass
       
cases=0    #initializing the number of cases 
while cases!=j:#while loop until the cases becoome equal to j
    l=int(input("Enter the number for which you want the next palindrome:--")) # Taking the input of number
    print(jojo())#Performs the above function and give the result
    cases+=1   #adding the cases with one until it is equal to j
