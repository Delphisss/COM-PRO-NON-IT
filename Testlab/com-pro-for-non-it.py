def m1(x,y):
    return x+y
def m2(x):
    z = []
    for i in range(len(x)-1):
        z.append(m1(x[i],x[i+1]))
    print(z)
    
test =[1,2,3,4,5]
m2(test)