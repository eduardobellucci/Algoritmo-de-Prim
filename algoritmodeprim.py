import queue
graph={'A':{'B':2,'C':4},
       'B':{'A':2,'C':2,'D':6},
       'C':{'A':3,'B':2,'D':3,'E':9},
       'D':{'B':3,'C':1,'E':2,'F':4},
       'E':{'C':8,'D':7,'F':6},
       'F':{'D':6,'E':5}}
def prim(graph,start):
    treepath={}
    total=0
    queue1=queue.PriorityQueue()
    queue1.push(0,(start,start))
    while queue1:
        weight,(node_start,node_end)=queue1.pop()
        if node_end not in treepath:
            treepath[node_end]=node_start
            if weight:
                print('added edge from %s'\
                    'to %s weighting %i'
                    %(node_start,node_end,weight))
                total+=weight
            for next_node,weight \
            in graph[node_end].items():
                queue.push(weight,(node_end,next_node))
    print('total spanning tree length:%i'%total)
    return treepath
treepath=prim(graph,'A')