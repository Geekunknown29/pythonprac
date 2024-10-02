
x = int(input("x"))
y = int(input("y"))
z = int(input("z"))
n = int(input("n"))
e= []  
for i in range (0,(x+1)):
    for j in range (0,(y+1)):
        for k in range (0,(z+1)):
            s = i+j+k
            if s != n:
                l = [i,j,k]
                e.append(l)
                
                x = [c for c in e if s != n]
x.sort()
print(x)




                    

                
    
