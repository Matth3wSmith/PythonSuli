from collections import defaultdict
import sys
sys.setrecursionlimit(20000)

def tarjans_scc(graph, n, start):
    index = 0
    stack = []
    indices = [-1] * n
    lowlink = [-1] * n
    on_stack = [False] * n
    scc = []
    reachable_from_start = set()

    def dfs(v):
        nonlocal index
        indices[v] = lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack[v] = True

        for w in graph[v]:
            if indices[w] == -1:
                dfs(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], indices[w])

        if lowlink[v] == indices[v]:
            component = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                component.append(w)
                if w == v:
                    break
            scc.append(component)
            if start in component:
                reachable_from_start.update(component)

    for i in range(n):
        if indices[i] == -1:
            dfs(i)

    return scc, reachable_from_start

# Bemenet olvasása
n, m, k = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)

# SCC meghatározása
scc, reachable = tarjans_scc(graph, n, k - 1)

# Lehetséges célpontok meghatározása
results = sorted(v + 1 for comp in scc for v in comp if v in reachable)
print(len(results))
if results:
    print(" ".join(map(str, results)))
else:
    print(0)