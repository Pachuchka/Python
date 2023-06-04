def in_power(n,m, pow = 1):
    if m==0:
        return pow
    else:
        return in_power(n,m-1,pow*n)

print(in_power(3,3))
