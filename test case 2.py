Sbase = int(input("Enter the base salary : "))
Sbonus = int(input("Enter the base bonus : "))
Sallowance = int(input("Enter the allowances : "))
E = int(input("Enter the expenditure : "))
Stotal = Sbase+Sbonus+ Sallowance
S=Stotal-E
if 0<= Sbase<= 2**31 - 1 and 0<= Sbonus<= 2**31 - 1 and 0<= Sallowance<= 2**31 - 1 and 0<= E <=2**31 - 1 :
    if Stotal == 0:
        P = 0.0
    else:
        P = (S / Stotal) * 100
else:
    print("Enter a valid data")
print("Total Salary:", Stotal)
print("Savings:", S)
if P==0:
    print("Savings Percentage: undefined ")
else:
    print(f"Savings Percentage: {P:.2f}")
