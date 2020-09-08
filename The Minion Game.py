def minion_game(string):
    vowel = ["A","E","I","O","U"]
    s = 0
    k = 0
    for i in range(len(string)):
        if string[i] in vowel:
            k = k+len(string)-i
        else:
            s = s+len(string)-i
    if s>k:
        print("stuart"+" "+"%d" %s)
    elif k>s:
        print("kevin"+" "+"%d" %k)
    else:
        print("Draw")
    

string = "BANANA"
minion_game(string)
