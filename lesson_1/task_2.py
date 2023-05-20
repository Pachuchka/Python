n = input('введите трёхзначное целое число: ')
n=int(n)
sum=0
while n>=1:
    sum = sum+n%10
    n = int(n/10)
print(sum)

