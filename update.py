n = int(input())
N = set(map(int,input().split()))
no = int(input())
for x in range(no):
    z = input().split()
    if z[0] == "intersection_update":
        new = set(map(int,input().split()))
        N.intersection_update(new)
    if z[0] == "update":
        new = set(map(int,input().split()))
        N.update(new)
    if z[0] == "symmetric_difference_update":
        new = set(map(int,input().split()))
        N.symmetric_difference_update(new)
    if z[0] == "difference_update":
        new = set(map(int,input().split()))
        N.difference_update(new)
print(sum(N))
    
        
