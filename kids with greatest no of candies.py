candies = list(map(int, input().split()))
extraCandies = int(input())

maxi = max(candies)
ans = []

for candy in candies:
    ans.append(candy + extraCandies >= maxi)

print(ans)