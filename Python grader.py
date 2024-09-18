
p=float(input("total points possible:"))
a=float(input("points achived:"))
s=(a/p)
if 1>s>0.89:
    print("A")
elif 0.88>s>0.76:
    print("B")
elif 0.76>s>0.61:
    print("C")
elif 0.60>s>0.51:
    print("D")
elif 0.5>s:
    print("F")
else:
    print("A+")