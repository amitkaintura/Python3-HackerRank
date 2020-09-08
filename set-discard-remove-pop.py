n = int(input())
s = set(map(int, input().split()))
N = int(input())
for x in range(N):
    strings = input().split()
    if strings[0]=="pop":
        s.pop()
    elif strings[0]=="remove":
        s.remove(int(strings[1]))
    elif strings[0]=="discard":
        s.discard(int(strings[1]))
print(sum(s))
