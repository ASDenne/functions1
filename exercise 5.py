def check_factor(num1, num2):
    if num1 % num2 == 0:
        print(f"{num2} is a factor of {num1}")
    else:
        print(f"{num2} isn't a factor of {num1}")
while True:
    num1 = int(input("enter a number      "))
    num2 = int(input("enter another number"))
    check_factor(num1, num2)

