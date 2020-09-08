def count_substring(string, sub_string):
    n = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            n = n+1
    return n
print(count_substring("abcdcdcdc","dc"))
