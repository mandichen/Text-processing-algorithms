import numpy as np
#from numpy import nan as NA
import pandas as pd

def edit_distance(x,y,sam,sub,de,ins):
    m=len(x)+1
    n=len(y)+1
    t = np.zeros((m,n))
    #initiate step
    for i in range(1,m):
        t[i][0]=t[i-1][0]+de
    for j in range(1,n):
        t[0][j]=t[0][j-1]+ins

    for i in range(1,m):
        for j in range(1,n):
            if x[i-1]==y[j-1]:
                t[i][j]=t[i-1][j-1]+sam
            else:
                sub_move=t[i-1][j-1]+sub
                del_move=t[i-1][j]+de
                ins_move=t[i][j-1]+ins
                t[i][j]=max(sub_move,del_move,ins_move) #min/max might be vary
    return pd.DataFrame(t,columns=["-"]+[k for k in y],index=["-"]+[k for k in x],dtype=int)

def local_distance(x,y,sam,sub,de,ins):
    m=len(x)+1
    n=len(y)+1
    s = np.zeros((m,n))

    for i in range(1,m):
        for j in range(1,n):
            if x[i-1]==y[j-1]:
                sub_move=s[i-1][j-1]+sam
            else:
                sub_move=s[i-1][j-1]+sub
            del_move=s[i-1][j]+de
            ins_move=s[i][j-1]+ins
            s[i][j]=max(sub_move,del_move,ins_move,0)
    return pd.DataFrame(s,columns=["-"]+[k for k in y],index=["-"]+[k for k in x],dtype=int)

def gap_alignment(x,y,sub,sam,f,h):
    m=len(x)+1
    n=len(y)+1
    de = np.zeros((m,n))
    ins = np.zeros((m,n))
    t = np.zeros((m,n))
    de[0][0]=99
    ins[0][0]=99
    t[1][0]=f
    t[0][1]=f
    for i in range(1,m):
        de[i][0]=99
        ins[i][0]=99
        if i>1:
            t[i][0]=t[i-1][0]+h    #f+(i+1-1)*h
    for j in range(1,n):
        de[0][j]=99
        ins[0][j]=99
        if j>1:
            t[0][j]=t[0][j-1]+h #f+(j+1-1)*h

    for j in range(1,n):
        #de[0][j]=99
        #ins[0][j]=99
        for i in range(1,m):
            de[i][j]=min(de[i-1][j]+h,t[i-1][j]+f)
            ins[i][j]=min(ins[i][j-1]+h,t[i][j-1]+f)
            if x[i-1]==y[j-1]:
                t[i][j]=min(t[i-1][j-1]+sam,de[i][j],ins[i][j])
            else:
                t[i][j]=min(t[i-1][j-1]+sub,de[i][j],ins[i][j])

    de = pd.DataFrame(de,columns=["-"]+[k for k in y],index=["-"]+[k for k in x],dtype=int)
    ins = pd.DataFrame(ins,columns=["-"]+[k for k in y],index=["-"]+[k for k in x],dtype=int)
    t=pd.DataFrame(t,columns=["-"]+[k for k in y],index=["-"]+[k for k in x],dtype=int)
    return de,ins,t




test2=edit_distance("GATTACA","GCATGCU",1,-1,-1,-1)
test3=local_distance("GATTACA","GCATGCU",1,-1,-1,-1)
print("examples:")
print()
print("local distance:")
print(test3)
print("global distance:")
print(test2)
print()
test5=edit_distance("AGTACGCA","TATGC",2,-1,-2,-2)
print(test5)
print()
test6=edit_distance("AGTA","TATGC",2,-1,-2,-2)
print(test6)
print()
test7=edit_distance("ACGC","CGTAT",2,-1,-2,-2)
print(test7)
