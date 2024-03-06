def y(w,c1,c2):
    for i in range(w):
        for j in range(w):
            if i >w/2 and j>w/2:
                print(c1, end='')
            else:
                print(c2, end='')
        print()
        
y(4,'x','o')