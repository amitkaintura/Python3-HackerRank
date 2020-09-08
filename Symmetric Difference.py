m = int(input())
m1 = set(map(int,input().split()))
n = int(input())
n1 = set(map(int,input().split()))
sym_diff = m1.symmetric_difference(n1)
result = list(sym_diff)
result.sort()
for x in result:
    print(x)
