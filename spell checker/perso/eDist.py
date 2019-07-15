import sys

def func(x, y):
    #print(x," and ",y)
    ### initialisation de la matrice ####
    a=[[10000] * (len(x)+1) for i in range((len(y)+1))]
    i=0
    for k in a:
        a[i][0]=i
        i=i+1
    i=0
    for k in a[0]:
        a[0][i]=i
        i=i+1

    #############################################
    
    k=1
    for i in x:
        r=1
        for j in y:
            #print("pour",k,"et",r)
            #print("nous somme dans: ",a[r][k])
            #print("replace:",a[r-1][k-1])
            #print("delete:",a[r][k-1])
            #print("insert:",a[r-1][k])
            min=getMin(a[r-1][k-1],a[r][k-1],a[r-1][k])
            #print(min)
            if j==i:
                a[r][k]=min
            else:
                a[r][k]=min+1
            r=r+1
        k=k+1
    #print(a)
    return a[len(y)][len(x)]

def getMin(a,b,c):
    if(a<b):
        if(a<c):
            return a
        else:
            if(b<c):
                return b
            else:
                return c 
    else:
        if b<c:
            return b
        else:
            return c



    
