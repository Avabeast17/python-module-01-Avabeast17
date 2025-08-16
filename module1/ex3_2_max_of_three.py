a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
m = a if a >= b and a >= c else b if b >= c else c
print(m)
