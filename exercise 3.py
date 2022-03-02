def check_status(bmi):
    if bmi < 18.5:
        status = "underwieght"
    elif bmi < 25:
        status = "normal"
    elif bmi < 30:
        status = "overwieght"
    else:
        status = "obese"
    return status
while True:
    wieght = float(input("enter wieght"))
    status = check_status(wieght)
    print(status)
