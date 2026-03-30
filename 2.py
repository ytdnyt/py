'''
要求：
如果输入的成绩在90分以上（含90分），则输出A；
输入的成绩在80分到90分之间（不含90分）则输出B；
输入的成绩在70分到80分之间（不含80分），则输出C；
输入的成绩在60分到70分之间（不含70分），则输出D；
输入的成绩在60分以下，则输出E。
'''
score=int(input('score='))
if score>=90:
    print('A')
elif 80<=score<90:
    print('B')
elif 70<=score<80:
    print('C')
elif 60<=score<70:
    print('D')
else:
    print('E')