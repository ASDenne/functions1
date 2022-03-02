def start_with_A(word):
    if word[0] == "A":
        return "True"
    else:
        return "False"
while True:
    word = input("enter word").upper()
    Astart = start_with_A(word)
    print(Astart)
