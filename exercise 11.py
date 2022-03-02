def libary_fine(days):
    price = days * .8 + .5
    if price < 30:
        return price
    else:
        return 30
#main
days = float(input("how long overdue is it"))
cost = libary_fine(days)
print(cost)
