p=float(input("Principal amount "))
r=float(input("Rate "))
t=float(input("Time "))
amount=p*(1+r/100)**t
Ci=amount-p
print("Compund Intrest is :-1",round(Ci,2))