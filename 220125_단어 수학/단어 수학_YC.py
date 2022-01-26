N = int(input())

importance={}
words=[]

for _ in range(N):
    word = list(input())
    words.append(word)
    for i, w in list(enumerate(reversed(word))):
        if w in importance:
            importance[w]+=10**i
        else:
            importance[w] = 10**i

dictionary={}

sorted_importance= {k: v for k, v in sorted(importance.items(), key=lambda item: item[1], reverse=True)}

num=9
for alp in sorted_importance:
    dictionary[alp] = num
    num-=1

answer=0
for word in words:
    for i, w in list(enumerate(reversed(word))):
        answer+=(dictionary[w]*10**i)
print(answer)