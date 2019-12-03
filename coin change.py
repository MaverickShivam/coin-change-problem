domina=[10,5,2,1]
ncoins=[8,5,6,10]
def num_coins(cents):
    mincoin=0
    temp=[]
    for i in range(0,len(ncoins)):
        temp.append(ncoins[i])
    for i in range(0,len(domina)):
        n=int((cents)/(domina[i]))
        if(n<=ncoins[i]):
            ncoins[i]=ncoins[i]-n
            cents=cents%domina[i]
        else:
            n=ncoins[i]
            ncoins[i]=0
            cents=cents-(n*domina[i])
        print(n,end=" ")
        mincoin=mincoin+n
    print()
    if(cents==0):
        #print(mincoin)
        print()
    else:
        for i in range(0,len(temp)):
            ncoins[i]=temp[i]
        print("Not Enough Coins")

num_coins(22)
num_coins(22)
num_coins(22)
num_coins(22)
num_coins(22)
num_coins(22)
print("---------",ncoins)



