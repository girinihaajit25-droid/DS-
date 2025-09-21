cp = float(input("Enter the cost price : "))
sp = float(input("Enter the selling price : "))
p = sp - cp
if cp < 0 or sp < 0:
    print("Cost price and selling price must be positive.")
else:
    if p > 0:
        print("Profit")
        print("Result : ",p)
    elif p < 0:
        print("Loss")
        print("Result : ",p)
    else:
        print("Break-even")
