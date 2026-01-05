#### Check wheather the given parenthesis is valid or not #######

def parenthesis_check(strs):
    stack=[]
    
    for chars in strs:
        
        if chars=="(" or chars =='{' or chars=='[':
            print(stack,chars)
            stack.append(chars)
            
        elif chars==')':
            if not stack or stack.pop() != '(' :
                return 1,False
        elif chars=='}':
            if not stack or stack.pop() != '{':
                return 2,False
        elif chars==']':
            if not stack or stack.pop() != '[':
                return 3,False
    #print(stack)
    return stack==[]
strs="({[]})"

print(parenthesis_check(strs))
    