from queue import PriorityQueue
v = 8
graph = [[] for i in range(v)]



# Function For Implementing Best First Search
# Gives output path having lowest cost


def best_first_search(actual_Src, target, n):
  visited = [False] * n
  pq = PriorityQueue()
  pq.put((0, actual_Src))
  visited[actual_Src] = True
  
  while pq.empty() == False:
    u = pq.get()[1]
    # Displaying the path having lowest cost
    print(u, end=" ")
    if u == target:
      break

    for v, d in graph[u]:
      if visited[v] == False:
        visited[v] = True
        pq.put((d, v))
  print()
def addedge(a, b, cost):
  graph[a].append((b, cost))
  graph[b].append((a, cost))
addedge(0, 1, 7)
addedge(0, 2, 15)
addedge(1, 3, 28)
addedge(3, 4, 17)
addedge(2, 3, 9)
source = 0
target = 4
best_first_search(source, target, v)