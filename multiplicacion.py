#ciclos

def multi(a,b):
    res=0
    for i in range(b):
        res=a+res
    return res

print(multi(0,3))    


#recursiva

def multi_recursiva(a,b):
    if b==0:
        return 0
    elif b>0:
        return a+multi_recursiva(a,b-1)
    else:
        return -multi_recursiva(a,-b)
    
print(multi_recursiva(5,-5))
     

