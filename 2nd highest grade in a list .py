

def list():
    global x
    global y
    x = input("name")
    y = float(input("marks"))
    l = [x,y]
    global flag
    flag = flag+1
    data.append(l)
data = []
N = int(input("N:"))
flag = 0
while flag <N :
    list()

print (data)
fil = []

for i in data :
    num = i[1]
    print(num)
    fil.append(num)
    mn= min(fil)
la = []
for mn in i :
    while mn is i[1]:
        print (i[0])
        la.append(i[0])
        break
        
            
print(la)           
print (mn)


