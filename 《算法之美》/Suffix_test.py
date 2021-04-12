def Suffix(arr):
    stack = []
    L = []
    for value in arr:
        if value == '(':
            stack.append(value)
        elif value == ')':
            s_n = len(stack) - 1
            while s_n != -1 and stack[s_n] != '(':
                L.append(stack.pop())
                s_n -= 1
            if stack != []:
                stack.pop()
        elif ord(value) >=48 and ord(value) <= 57:
            L.append(value)
        else:
            s_n = len(stack) - 1
            while s_n != -1 and stack[s_n] != '(':
                if stack[s_n] == '*' or stack[s_n] == '/':
                    if stack[s_n] == value:
                        L.append((stack.pop()))
                else:
                    break
                s_n -= 1
            stack.append(value)
    while stack != []:
        L.append(stack.pop())
    return L


if __name__ == '__main__':
    formula = '3/(6*4/3*8)'
    L = Suffix(formula)
    print(L)
