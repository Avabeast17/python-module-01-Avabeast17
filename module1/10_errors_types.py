raw = input("Enter a number: ")
try:
    val = float(raw)
    print(val / 2)
except ValueError:
    print("Not a number")
