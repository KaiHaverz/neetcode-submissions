class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        close_to_open={")":"(","}":"{","]":"["}

        for c in s:
            # 如果当前字符是右括号
            if c in close_to_open:
                # 栈不为空且栈顶元素恰好是对应的左括号
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop() # 匹配成功，弹出栈顶
                else:
                    return False # 栈空或者不匹配，直接失败
            else:
                # 如果是左括号，直接压入栈中
                stack.append(c)
        
        if not stack:
            return True
        else:
            return False