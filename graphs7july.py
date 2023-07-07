#graphs
def add_node(v):
    if v in graph:
        print("The given node is already present in graph")
    else:
        graph[v] = []
        
def add_edge(v1, v2):
    if v1 not in graph:
        print(v1, "is not present")
    if v2 not in graph:
        print(v2,"is not present")
    else:
        list1 = [v2]
        list2 = [v1]
        graph[v1].append(v2)
        graph[v2].append(v1)
        
def delete_node(v):
    if v not in graph:
        print("The given node v is not present in the graph")
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            if v in list1:
                list1.remove(v)
                
def delete_edge(v1,v2):
    if v1 not in graph:
        print(v1,"is not present")
    if v2 not in graph:
        print(v2,"is not present")
    else:
        if v1 in graph[v2]:
            graph[v2].remove(v1)
        if v2 in graph[v1]:
            graph[v1].remove(v2)
                
def DFS(node, graph):
    visited = set()
    if node not in graph:
        print("node is not present")
        return
    stack = []
    stack.append(node)
    print("DFS order is")
    while stack:
        current = stack.pop()
        if current not in visited:
            
            print(current, end = " ")
            visited.add(current)
            for i in graph[current]:
                stack.append(i)


def BFS(node,graph):
    visited = set()
    if node not in graph:
        print("node is not present in graph")
        return
    queue = []
    queue.append(node)
    print("BFS order is")
    while queue:
        m = queue.pop(0)
        print(m, end = " ")
        visited.add(m)
        for n in graph[m]:
            if n not in visited:
                visited.add(n)
                queue.append(n)
    
                
graph = {}
print("the graph is:",graph)
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_edge("A","B")
add_edge("A","D")
add_edge("A","E")
add_edge("D","C")
#delete_node("A")
#delete_edge("A","B")
print(graph)
print(graph.keys())
DFS("A",graph)
print()
BFS("A",graph)
