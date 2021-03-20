a = eval(input("Enter the first number/expression:"))
print(a)
b = eval(input("Enter the second number/expression:"))
print(b)
c = eval(input("Enter the third number/expression:"))
print(c)
if a > b and b > c:
    if b > c:
        print(a, '>', b, '>', c)
    else:
        print(a, '>', c, '>', b)
elif b > c and b > a:
    if c > a:
        print(b, '>', c, '>', a)
    else:
        print(b, '>', a, '>', c)
elif c > a and c > b:
    if a > b:
        print(c, '>', a, '>', b)
    else:
        print(c, '>', b, '>', a)
