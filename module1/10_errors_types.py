raw = input("Enter a number: ")
try:
    val = float(raw)
    print("Half is", val / 2)
except ValueError:
    print("That was not a number.")
