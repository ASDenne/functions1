def check_factor(list):
    longest_length = 0
    longest_word = ""
    for words in range(0, len(list)):
        length = 0
        for length_ in range(0, len(list[words])):
            length += 1
        if length > longest_length:
            longest_length = length
            longest_word =list[words]
    print(longest_word)




#main
list = ["dog", "cat", "sheep", "dot", "catch"]
check_factor(list)

