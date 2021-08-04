coins = int(input())
tc = []
tc = list(map(int, input().split(' ')[:coins]))
tc.sort(reverse=True)
total = sum(tc)
a = 0
b = 0
while (a <= total // 2):
    a += tc[b]
    b += 1
print(b)