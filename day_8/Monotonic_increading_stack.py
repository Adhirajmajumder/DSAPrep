##### Monotonic Stack #####

def monotonic_increasing_stack(array):
    stack=[]
    N=len(array)
    ans=[-1]*N
    for i in range(N):
        while stack and array[stack[-1]]>array[i]:
            idx = stack.pop()
            ans[idx] = array[i]
        stack.append(i)
    return stack
    
array= [8, 4, 6, 2, 5]
print(monotonic_increasing_stack(array))
        