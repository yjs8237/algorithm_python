import sys

sys.stdin = open("./input/3.txt" , 'rt')
a=list(range(21))

for _ in range(10):
    s, e = map(int , input().split())
    print(s , e)
    for i in range((e-s+1) // 2):
        a[s+i], a[e-i]=a[e-i] , a[s+i]

a.pop(0)
print(a)