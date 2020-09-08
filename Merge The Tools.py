def merge_the_tools(string, k):
    n =len(string)
    string_list = []
    for i in range(0,n,k):
        sub_string = string[i:i+k]
        short_string =""
        for j in sub_string:
            if j not in short_string:
                short_string+=j
        string_list.append(short_string)
    print(*string_list,sep ="\n")
string = "AACABCABCF"
k = 3
merge_the_tools(string,k)
