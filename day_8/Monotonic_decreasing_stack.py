#### Monotonically Decreaseing Stack ####

def monotonically_decreasing_stack(array):
    stack=[]
    N=len(array)
    ans=[-1]*N
    
    for i in range(N):
        while stack and array[stack[-1]]<array[i]:
            idx=stack.pop()
            ans[idx]=array[i]
        stack.append(i)
    return ans

array = [9, 3, 7, 1, 4]

print(monotonically_decreasing_stack(array))