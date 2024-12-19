runtime = int(input())
while runtime > 0:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    test_case = (str(input())).lower()
    for i in test_case:
        if i in alphabet:
            alphabet.pop(alphabet.index(i))
        else:
            pass
    missing = ""
    for i in alphabet:
        missing += i
    
    if alphabet == []:
        print("pangram")
    else:
        print("missing" + " " + str(missing))
    runtime -= 1
    