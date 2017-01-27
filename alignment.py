import numpy as np
#from numpy import nan as NA
import pandas as pd

def edit_distance(x,y,sub,de,ins):
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
                t[i][j]=t[i-1][j-1]
            else:
                sub_move=t[i-1][j-1]+sub
                del_move=t[i-1][j]+de
                ins_move=t[i][j-1]+ins
                t[i][j]=min(sub_move,del_move,ins_move)
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



test1=edit_distance("EAWACQGKL","ERDAWCQPGKWY",3,1,1)
test2=edit_distance("ACGA","ATGCTA",1,1,1)
test3=local_distance("EAWACQGKL","ERDAWCQPGKWY",1,-3,-1,-1)
print("global distance:")
print(test1)
print()
print(test2)
print()
print("local distance:")
print(test3)
