#This program is for the utility agent that chooses the minimum cost path from source to destination.
def name(n):
    if n==0:
        return 'A'
    elif n==1:
        return 'B'
    elif n==2:
        return 'C'
    elif n==3:
        return 'G'
    
def costcheck(cost): 
   if cost==0:
       return 'No direct cost given'
   else:
       return cost 

def total(i,j,k):
    print("\nCost for ",name(i),"-",name(j),"-",name(k))
    print(name(i),"-",name(j),": Rs.",costs[i][j])
    print(name(j),"-",name(k),": Rs.",costs[j][k])
    print("Total Cost= ",costs[i][j]+costs[j][k])
    return costs[i][j]+costs[j][k]
    
   
costs=[[1,5,8,0],
       [0,3,10,7],
       [7,1,2,9],
       [1,4,8,0]]
print("\nTotal cost required in this path is  \n")
for i in range(0,4):
    for j in range(0,4):
        if i>=j:
            pass
        else:
            print(name(i)," to ",name(j)," = ",costcheck(costs[i][j])) 
print("\nCost in the undefined path (B to C) : ")
print("B--> G--> C : ",costs[1][3]+costs[3][2])
print("B--> A--> C : ",costs[1][0]+costs[0][2])

## Checking for the shortest path
print("\nFinding optimal path from A to G")
a=total(0,1,3)
b=total(0, 2, 3)
if min(a,b)==a:
    print("\nCost for A-->B-->G is Rs. ", a,"  which is minimum.\n Utility Agent selects this path.")
else:
    print("\nCost for A-->C-->G is Rs. ", b," which is minimum. \n Ulility Agent selects this path.")