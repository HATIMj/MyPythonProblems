

                                                       #Matches founder

def matcher(s1,s2):
    """This function takes two sentences and matches the every word of first sentence with every word of the other sentence"""
    sen1=s1.split(" ")
    sen2=s2.split(" ")
    score=0
    for i in sen1:
        for j in sen2:
            if i.lower()==j.lower():
                score+=1
    return score
if __name__=="__main__":
    sen=["python is good","this is good","who is this","he is a human"]    #List
    i=input()  #sentence input
    l=[matcher(i,se) for se in sen]    #Matches found in the above list
    m=[l for l in reversed(sorted(zip(l,sen)))]  #Taking the matches and the parallel sentences together
    for score,item in m:
        print(f"{item}: with a score of {score}")  #Printing the sentences according to myself