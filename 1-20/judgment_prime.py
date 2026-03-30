num=int(input('num='))
end=int(num**0.5+1)
if num==2:
    print('prime')
else:
    for i in range(2,end):
        if num%i==0:
            print('not prime')
            break
    else:
        print('prime')
