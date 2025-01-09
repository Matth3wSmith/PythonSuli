from sys import stdin,stdout
id=0
scc=0
def dfs(at):
    global id
    global scc
    stack.append(at)
    stackben[at] = True
    id=id+1
    ids[at] = lowlink[at] = id
    #Minden szomszéd meglátogatása és a minimum lowlink beállítása visszatéréskor
    for to in g[at]:
        if ids[to] == -1:
            dfs(to)
        if stackben[to]:
            lowlink[at]=min(lowlink[at],lowlink[to])
    
    #Miután minden szomszádját megnéztük az "at"-nek
    #ha az elején vagyunk a SCC-nek akkor kiürítjük
    #a stacket amíg nem vagyunk a SCC elején
    if ids[at]==lowlink[at]:
        for node in stack:
            stack.remove(node)
            stackben[node]=False
            lowlink[node]=ids[at]
            if node==at: 
                break
        scc+=1

def main():
    pontSzam,szakaszSzam,kezdopont=map(int,stdin.readline().split())
    global g
    g=[[] for __ in range(pontSzam+1)]
    for __ in range(szakaszSzam):
        sor=list(map(int,stdin.readline().split()))
        g[sor[0]].append(sor[1])

    global ids
    global lowlink
    global stackben
    global stack
    ids=[-1]*(pontSzam+1)
    lowlink=[0]*(pontSzam+1)
    stackben=[False]*(pontSzam+1)
    stack=[]

    for i in range(pontSzam):
        if ids[i]==-1:
            dfs(i)

    print(lowlink)
    print(scc)

main()