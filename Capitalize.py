def solve(s):
    new2 = []
    new = s.split(" ")
    for x in range(len(new)) :
        t = new[x].capitalize()
        new2.append(t)
    return(' '.join(new2))


z ="1 2 2 3 4 5 6 7 8   9"
print(solve(z))
 
 
