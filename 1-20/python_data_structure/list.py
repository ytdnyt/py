'''
items=[11,11,12,13]
print(type(items))  #<class 'list'>
'''


'''
items4 = list(range(1, 10))
items5 = list('hello')
print(items4)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(items5)  # ['h', 'e', 'l', 'l', 'o']

print(9 in items4)  # True
print(9 not in items4)  # False
print(items4[2])    # 3
items4[1]=1
print(items4)   # [1, 1, 3, 4, 5, 6, 7, 8, 9]
print(items4[1:5:2])    # [1, 4]
#[1, 2] < ['a', 'b']   # ❌ TypeError
print([1, 2] == ['a', 'b']) #False
'''

'''
languages = ['Python', 'Java', 'C++', 'Kotlin']
for i in languages:
    print(i)
'''

'''
掷骰子 
'''
import random

counts=[0]*6
# 模拟掷色子记录每种点数出现的次数
for _ in range(600):
    face=random.randrange(1,7)
    counts[face-1]+=1
# 输出每种点数出现的次数
for face in range(1,7):
    print(f'{face}点出现了{counts[face-1]}次')