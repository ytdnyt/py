x=float(input('x='))
if x>1:
    y=3*x-1
elif -1<=x<=1:
    y=x+2
elif x<-1:
    y=5*x+35
print(f'y={y}')
