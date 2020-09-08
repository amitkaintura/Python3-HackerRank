def average(array):
    new = set(array)
    return sum(new)/len(new)
array = eval(input())
print(average(array))
