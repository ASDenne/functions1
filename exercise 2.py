def make_positive(input):
    output = abs(input)
    return output
while True:
    number = int(input("enter number"))
    positive_number = make_positive(number)
    print(positive_number)
