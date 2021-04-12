"""
@Date: Tuesday, 16 March, 2021
@Author: Chen Zhang
@Brief: 自己写的中缀表达式转换算法无法通过调试

https://www.nowcoder.com/practice/9999764a61484d819056f807d2a91f1e?tpId=37&tqId=21273&rp=1&ru=%2Fta%2Fhuawei&qru=%2Fta%2Fhuawei%2Fquestion-ranking&tab=answerKey

出错用例：3*5+8-0*3-6+0+0
"""
formula = list(input())
S = []
L = []
n = len(formula)
for i in range(n):
    if formula[i] in ['{', '[', '(']:
        S.append(formula[i])
    elif formula[i] in ['+', '-']:
        if formula[i] == '-' and formula[i-1] in ['{', '[', '(']:
            formula[i+1] = '-'+formula[i+1]
        else:
            if len(S) != 0:
                if formula[i] == '-':
                    j = len(S)-1
                    while S[j] in ['*', '/', '-']:
                        L.append(S.pop())
                        j -= 1
                        if j < 0:
                            break
            else:
                S.append(formula[i])
    elif formula[i] in ['*', '/']:
        S.append(formula[i])
    elif formula[i] == '}':
        j = len(S)-1
        while S[j] != '{':
            L.append(S.pop())
            j -= 1
        S.pop()
    elif formula[i] == ']':
        j = len(S)-1
        while S[j] != '[':
            L.append(S.pop())
            j -= 1
        S.pop()
    elif formula[i] == ')':
        j = len(S)-1
        while S[j] != '(':
            L.append(S.pop())
            j -= 1
        S.pop()
    else:
        L.append(formula[i])
for i in range(len(S)-1, -1, -1):
    L.append(S.pop())

N = []
for i in range(len(L)):
    try:
        num = int(L[i])
        N.append(num)
    except:
        if L[i] == '+':
            b = int(N.pop())
            a = int(N.pop())
            N.append(a+b)
        elif L[i] == '-':
            b = int(N.pop())
            a = int(N.pop())
            N.append(a-b)
        elif L[i] == '*':
            b = int(N.pop())
            a = int(N.pop())
            N.append(a*b)
        else:
            b = int(N.pop())
            a = int(N.pop())
            N.append(a/b)
print(N.pop())

