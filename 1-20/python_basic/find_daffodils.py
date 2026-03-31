'''
要求：找出 100 到 999 范围内的所有水仙花数。
它是一个N位非负整数，其各位数字的N次方和刚好等于该数本身
'''
for i in range(100,1000):
    basicunit=i%10
    tensplace=i//10%10
    hundred=i//100
    add=basicunit**3+tensplace**3+hundred**3
    if add==i:
        print(i)