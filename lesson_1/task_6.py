n = input('введите шестизначный номер билета номер билета: ')
n=int(n)
while n < 99999 or n > 999999:
    n = input('номер должен быть шестизначным: ')
    n = int(n)    
a = int(n/1000)
b = int(n -a*1000)

sum_1=0
while a>=1:
    sum_1 = sum_1+a%10
    a = int(a/10)


sum_2=0
while b>=1:
    sum_2 = sum_2+b%10
    b = int(b/10)

if sum_1==sum_2:
    print(True)
else:
    print(False)
