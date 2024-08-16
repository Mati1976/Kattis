num = int(input())

first=1
second=2
if num == 1:
    new = 1
elif num == 2:
    new = 2

for i in range(2,num) :
    new = first + second + 1
    first = second
    second = new

print(new)
