def balance():
    while True:
        line = input()
        if line == '.':
            break
        flag = True
        stack = []
        for c in line:
            if c == "[" or c == "(":
                stack.append(c)
            elif c == "]":
                if not stack or stack.pop() != "[":
                    flag = False
                    break
            elif c == ")":
                if not stack or stack.pop() != "(":
                    flag = False
                    break
        if stack:
            flag = False
        if flag:
            print("yes")
        else:
            print("no")

balance()