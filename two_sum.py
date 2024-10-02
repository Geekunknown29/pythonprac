nums = []
target = int(input("target : "))
N = int (input ("N : "))
ans = []
 
flag = 0 
for flag in range (N) :
    i = int (input ("your input no . : ") )
    for g in range (flag) :
        if i == nums[g] :
            print ("same values can not be given more than once")
            break
    nums.append(i)
    flag = flag+1
"""
for q in range (0,len(nums)):
    for z in range (0,len(nums)):

        if nums[q]==nums[z]:
            nums.pop(nums[q])
"""

for x in range (0,len(nums)) :
    for y in range (0,len(nums)) :
        if nums [x] + nums[y] == target :
            ans.append(x)
            ans.append(y)
            continue
'''for w in range (len(ans)) :
    for r in range (len(ans)) :
        if ans[w] == ans[r] :
            ans.pop(w)
#   '''          
print (ans)

# while True :
for n in ans :
    for m in ans :
        if m == n :
            ans.remove(m)

print(ans)
        