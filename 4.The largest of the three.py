a = eval(input("Enter the first number/expression:"))
print(a)
b = eval(input("Enter the second number/expression:"))
print(b)
c = eval(input("Enter the third number/expression:"))
print(c)
if a > b and a > c:
    print(a,'is the largest')
elif b > c and b > a:
    print(b,'is the largest')
else:
    print(c,'is the largest')