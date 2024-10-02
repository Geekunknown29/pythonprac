N = int(input("number of entries : "))
flag = 0
R = {}

while flag < N :
    data = input("name and marks : ")
    D = data.split(" ")
    flag = flag +1
    print("data : " , data)
    print("D : ", D)
    num = []
    name = ''
    for i in D :
        if i == 0 :
            name.append(i)
        elif i != 0:
            num.append(i)
            

print ("name : ", name)
                   
print ('num : ', num)
R[name] = num

print (R)