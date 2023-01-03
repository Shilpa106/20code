# STDIN           Function
# -----           --------
# 3               n = 3
# {[()]}          first s = '{[()]}'
# {[(])}          second s = '{[(])}'
# {{[[(())]]}}    third s ='{{[[(())]]}}'

t = int(input().strip())
s=[]
for t_itr in range(t):
    s.append(input().split())
print(s)

#     result = isBalanced(s)

# def isBalanced(s):
    
    