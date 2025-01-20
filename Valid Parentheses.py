
def isValid(s = "(){}({()})[{()}]") -> bool:
    stack = []
    if len(s) % 2 != 0 :
        return False
    for c in  s:
        if c == "{" or c == "(" or c == "[":
            stack.append(c)
        else:
            if not stack:
                return False
            else:
                if c == "}" and stack[-1] == "{":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                elif c == ")" and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
    return (len(stack)==0)

print(isValid())