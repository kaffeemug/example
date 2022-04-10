from collections import deque


n,m,o = map(int, input().split())

g1 = []
g2 = []
v1 = []
v2=[]
q = deque()


g1 = [[0]*(n+1) for _ in range(n+1)]


def dfs(idx):
    v1.append(idx)
    print(idx, end=" ")
    for i in range(1,n+1):
        if (i not in v1) and (g1[idx][i] == 1):
            dfs(i)




def bfs(idx):
    q.append(idx)
    v2.append(idx)

    while q:
        v = q.popleft()
        print(v, end=" ")

        for i in range(1,n+1):
            if (i not in v2) and (g1[v][i] == 1):
                q.append(i)
                v2.append(i)


for _ in range(m):
    a, b = map(int, input().split())
    g1[a][b] = g1[b][a] = 1



dfs(o)
print()
bfs(o)
