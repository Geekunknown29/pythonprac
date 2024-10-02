'''
TAASK :-
take an input no. n and print all whole no. in a series
without any character between any two elements
consteraints : 1<=n<=150
example outpt:   12345...n (where n is the input no.)
'''

n = int(input(""))
if n>= 1 and n<= 150:
    for i in range (1,(n+1)):
        print(i,end = "")
