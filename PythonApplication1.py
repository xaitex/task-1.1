a = float(input("Enter a: "))
b = float(input("Enter b: "))

if a <= 0 or b <= 0:
    print("Error: a and b must be positive!")
else:
    if a > b:
        X = a / b - 1
    elif a == b:
        X = -25
    else:
        X = (a ** 3 - 5) / a

    print("Result X =", X)
