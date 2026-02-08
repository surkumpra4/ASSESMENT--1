a=float(input("Enter First Side"))
b=float(input("Enter Second Side"))
c=float(input("Enter third Side"))
sum=(a+b+c)/2
area=(sum*(sum-a)*(sum-b)*(sum-c))**0.5
print("area of triangle are:",round(area,2))