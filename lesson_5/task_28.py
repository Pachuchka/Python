def recurce_sum(n,m):
    if m==0:
        return n
    else:
        return recurce_sum(n+1,m-1)

print(recurce_sum(13,3))