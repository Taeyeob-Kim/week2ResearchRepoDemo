import random
lotto=[]
while len(lotto)<6:
    num=random.randint(1,40)
    if num not in lotto:
        lotto.append(num)
    
    print("the lotto numbers are", lotto)
    
    ## I bought a lotto last night and It passed my mind, I may could make code to pick numbers. And this is what I made. 
