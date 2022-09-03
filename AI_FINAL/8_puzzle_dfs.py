from copy import deepcopy

stack = [] # Using a list in python as a stack to perform the DFS search. 

visited = set() # A set to avoid reaching the previously visited state.

# To print the intermediate states while performing the BFS.

def print_current_state(a):
  for i in a:
    for j in i:
      print(j, end = " ")
    print()
  print()

def left(a):
  b = deepcopy(a);
  for i in range(len(b)):
    for j in range(len(b)):
      if a[i][j] == 0:
        if j - 1 >= 0:
          b[i][j - 1], b[i][j] = b[i][j], b[i][j - 1]
          c = tuple(map(tuple, b)) # Since lists are mutable it is required to be converted into some immutable container which can be used as a key in the dictionary. 
          if c in visited:
            return
          visited.add(c)
          stack.append(b)
          return

def right(a):
  b = deepcopy(a);
  for i in range(len(b)):
    for j in range(len(b)):
      if a[i][j] == 0:
        if j + 1 < len(b):
          b[i][j + 1], b[i][j] = b[i][j], b[i][j + 1]
          c = tuple(map(tuple, b))
          if c in visited:
            return
          visited.add(c)
          stack.append(b)
          return

def up(a):
  b = deepcopy(a);
  for i in range(len(b)):
    for j in range(len(b)):
      if a[i][j] == 0:
        if i - 1 >= 0:
          b[i - 1][j], b[i][j] = b[i][j], b[i - 1][j]
          c = tuple(map(tuple, b))
          if c in visited:
            return
          visited.add(c)
          stack.append(b)
          return

def down(a):
  b = deepcopy(a);
  for i in range(len(b)):
    for j in range(len(b)):
      if a[i][j] == 0:
        if i + 1 < len(b):
          b[i + 1][j], b[i][j] = b[i][j], b[i + 1][j]
          c = tuple(map(tuple, b))
          if c in visited:
            return
          visited.add(c)
          stack.append(b)
          return

def dfs(a, b):

  stack.append(a)

  count = 0
  
  while len(stack) is not 0:
    
    count += 1;

    now = stack.pop()

    print_current_state(now)

    if now == b:
      print("Reached destination at iteration ", count)
      return
    
    for i in range(len(now)):
      for j in range(len(now)):
        if now[i][j] == 0:
            right(now)
            up(now)
            down(now)
            left(now)
     
a = [[7, 2, 4], [5, 0, 6], [8, 3, 1]] # Initial State
b = [[0, 1, 2], [3, 4, 5], [6, 7, 8]] # Goal State

dfs(a, b) 