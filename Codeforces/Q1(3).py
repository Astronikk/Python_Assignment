a = []
for i in range(0, 5):
    a.append([int(j) for j in input().split()])


def find(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 1:
                return (abs(i - 2) + abs(j - 2))


print(find(a))