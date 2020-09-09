k = int(input())
n = list(map(int,input().split()))
s1 = set()
s2 = set()
for x in n:
    if x not in s1:
        s1.add(x)
    else:
        s2.add(x)
result = sum(s1)-sum(s2)
print(result)
