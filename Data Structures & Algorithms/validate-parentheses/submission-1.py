class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        for i in s:
            print(stack)
            if i == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif i == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if len(stack)==0:
            return True
        return False            
        
        