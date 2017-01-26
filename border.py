def compute_borders(x): #mp next
    border = []
    border.append(-1)
    for i in range(0,len(x)):
        j=border[i]
        while j>=0 and x[i]!=x[j]:
            j=border[j]
        border.append(j+1)
    return border

def computeKMP_next(x):  #kmp next
    kmp_next = []
    kmp_next.append(-1)
    k=0
    for i in range(1,len(x)):
        if x[i]==x[k]:
            kmp_next.append(kmp_next[k])
        else:
            kmp_next.append(k)
            while k>=0 and x[i]!=x[k]:
                k=kmp_next[k]
        k=k+1
    kmp_next.append(k)
    return kmp_next

#def searchWithSMA(x,y):




x = "abacabacab"
print(x)
print("MP_next table:")
print(compute_borders(x))
print("KMP_next table:")
print(computeKMP_next(x))
