print("Ingresa un numero pa")
num = int(input())


def isStep(n):
    a = map(int, str(n)[1:])
    b = map(int, str(n)[:-1])
    return all(abs(a_digit - b_digit) == 1 for a_digit, b_digit in zip(a, b))


if(isStep(num) == True):
    print("True😎")
else:
    print("False :(")
