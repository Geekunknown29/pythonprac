n = int(input("n"))
f= 0
score = []
while f< n :
    l = int(input("score"))
    score.append(l)
    f = f+1
print(score,"1")
score.sort()
print(score,"2")

for a in score:
    for b in score:
        if a is not b and a == b :
            score.pop(a)
print(score,"3")
""" mx = max(score)
    score.remove(mx)
    
    m2x = max(score)
    print(m2x)
    """

"""
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[arr.index(max(arr))-1])
"""
