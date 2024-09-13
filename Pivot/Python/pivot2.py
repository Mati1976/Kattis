size = int(input())
inp = list(map(int,input().split()))

count = size

maximum= [0] * (size-1)
minimum= [0] * (size-1)
res = [1] * (size-2)

maximum[0] = inp[0]
minimum[size-2] = inp[size-1]

for j in range (2,size):

    if inp[j-1] > maximum[j-2] :
        maximum[j-1] = inp[j-1]
    else :
        maximum[j-1] = maximum[j-2]
        count -= res[j-2]
        res[j-2] *= 0
      

    if inp[size-j] < minimum[size-j] :
        minimum[size-j-1] = inp[size-j] 
    else :
        minimum[size-j-1] = minimum[size-j]
        count -= res[size-1-j]
        res[size-1-j] *= 0


if inp[0] >= minimum[0] :
    count -= 1


if inp[size-1] <= maximum[size-2]:
    count -= 1
    

print(count)