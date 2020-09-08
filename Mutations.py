def mutate_string(string,position,character):
    list1 = list(string)
    list1[position]=character
    result = "".join(list1)
    return result
string = input()
position = int(input())
character = input()
print(mutate_string(string,position,character))
