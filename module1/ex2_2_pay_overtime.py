h = float(input("Hours: "))
r = float(input("Rate: "))
pay = h * r if h <= 40 else 40 * r + (h - 40) * r * 1.5
print(pay)
