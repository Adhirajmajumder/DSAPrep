### Generate Parenthese ###

def generate_parenthesis(n):
    res=[]
    
    def backtract(open_used, close_used, current):
        if open_used==n and close_used==n:
            res.append(current)
            return 
        
        if open_used<n:
            backtract(open_used+1, close_used, current+ "(")
        
        if close_used<open_used:
            backtract(open_used,close_used+1, current + ")")
    backtract(0,0,"")
    return res

print(generate_parenthesis(4))