for num in range(2,100):
    end=int(num**0.5)
    for i in range(2,end+1):
        if num%i==0:
            break
    else:
        print(num)
