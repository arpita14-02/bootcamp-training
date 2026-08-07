n = int(input())
sentences = []
for i in range(n):
    sentences.append(input())

maxi = 0

for sentence in sentences:
    words = len(sentence.split())
    if words > maxi:
        maxi = words
print(maxi)    