                                                                 #Searcher



j=input("Put the input query:").lower()#Taking input from user in lowecase 
k=["jojo is good","khojo is good","what is good and bad?"]  #List of sentences which will be used by program to find words
x=0   #setting the variable to 0
m=[]  #Making a new list
for i in (k[::-1]):  #Reversing the list order  as required
    
    if j in i:  #Searching every word of every element of list for a match 

        x+=1    #Adding 1 after every match found
        m.append(i)  #Append the matches to the new list
print(f"{x} results found")#Printing out the number of matches found 
for i in m:  #Iterating through the new list 
    print(i)#Print the list's elements
                                #----------------------------------------------------------------------------------------------#