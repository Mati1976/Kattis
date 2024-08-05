num= list(map(int,input().split()))
order = input()
answer = []
num.sort()
dict = {"A":num[0], "B":num[1], "C":num[2]}
for i in order:
    answer.append(str(dict.get(i)))
print(answer[0]+" "+answer[1]+" "+answer[2])

