p=int(input("enter the value principal amount:"))
r=float(input("enter the value of interest rate:"))
t=float(input("enter the time:"))
dur=input("enter years or months:")
if dur=="months" or dur=="Months":
    t=t/12
if 1<=p<=2**31-1 and 1<=r<=8.5:
    a=p*((1+r/100)**t)
    print("compound amount:",a)
else:
    print("enter valid data")
    
