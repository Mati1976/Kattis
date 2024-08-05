sol= {}
res = 0
count= 0
while True:
    inp=input().split()
    if inp[0] == '-1':
        break
    if inp[1] not in sol.keys() :
        if inp[2] == 'right':
            sol[inp[1]]=[int(inp[0]) , inp[2]]
        else:
            sol[inp[1]]=[20 , inp[2]]

    else:
        if inp[2] == 'right':
            sol[inp[1]]=[sol[inp[1]][0]+int(inp[0]),inp[2]]
        else:
            sol[inp[1]]=[sol[inp[1]][0]+20,inp[2]]
            

for key,value in sol.items():
    if value[1] == 'right':
        count += 1
        res += value[0]
print(count,res)
