size = int(input())
inp = list(map(int,input().split()))

count = 0

minimum = min(inp[1:size])
if inp[0] < minimum :
    count += 1

maximum = max(inp[0:1])
minimum = min(inp[2:size])
if ((inp[1] > maximum) and (inp[1] < minimum) ):
    count +=1

for j in range (2,size-1):
    if inp[j-1] > maximum :
        maximum = inp[j-1]
    
    minimum = min(inp[j+1:size])
    if ((inp[j] > maximum) and (inp[j] < minimum) ):
        count +=1

maximum = max(inp[0:size-1])

if inp[size-1] > maximum :
    count += 1 

print(count)
