a=int(input('a='))
b=int(input('b='))
if a>b:
    temp=a
    a=b
    b=temp
for i in range(1,a+1):
    if b%i==0 and a%i==0:
        common_divisor=i
print(common_divisor)
'''
欧几里得算法
x = int(input('x = '))
y = int(input('y = '))
while y % x != 0:
    x, y = y % x, x
print(f'最大公约数: {x}')
算法可以大大提高效率
'''