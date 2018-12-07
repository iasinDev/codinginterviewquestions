from collections import defaultdict
def connectedCities(n, g, originCities, destinationCities):
    connectedness_matrix = [[0 for i in range(n+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if i!=j and gcd(i, j) > g:    
                connectedness_matrix[i][j] = 1
                connectedness_matrix[j][i] = 1

    def bfs(a,b):
        queue=[]
        visited_nodes = [False] * (n+1)
        queue.append(a)
        while queue:
            node = queue.pop(0)
            if not visited_nodes[node]:
                visited_nodes[node] = True
                for i in range(n+1):
                    if connectedness_matrix[node][i] == 1 and not visited_nodes[i]:
                        queue.append(i)

            if node == b:
                return 1
        return 0

    result_list = []
    for i in range(len(originCities)):
        result = bfs(originCities[i], destinationCities[i])
        result_list.append(result)

    return result_list    

def gcd(a,b):
  while b!=0:
    r = a % b
    a = b
    b = r
  return a

print(connectedCities(6,2,[1,2,3], [4,5,6]) == [0,0,1])
print(connectedCities(6,0,[1,4,3,6], [3,6,2,5]) == [1,1,1,1])
print(connectedCities(6,1,[1,2,4,6], [3,3,3,4]) == [0,1,1,1])

# First version -> correct but too slow
#     
# def connectedCities(n, g, originCities, destinationCities):
#     # Write your code here
#     connected_nodes={}
#     for i in range(len(originCities)):
#         for j in range(len(destinationCities)):
#             if gcd(originCities[i], destinationCities[j]) > g:    
#                 connected_nodes[originCities[i]] = destinationCities[j]
#                 connected_nodes[destinationCities[j]] = originCities[i]

#     result_list = []
#     for i in range(len(originCities)):
#         result = dijkstra(connected_nodes, originCities[i], destinationCities[i])
#         result_list.append(result)

#     return result_list    
    
# def dijkstra(connected_nodes, a, b):
#     visited_nodes = []
#     queue=[]
#     queue.append(a)
#     while queue:
#         node = queue.pop(0)
#         if node not in visited_nodes:
#             visited_nodes.append(node)
#             for k,v in connected_nodes.items():
#                 if k == node:
#                     queue.append(v)
#                 if v == node:
#                     queue.append(k)

#         if node == b:
#             return 1
#     return 0

# def gcd(a, b):  
#     if a == 0 : 
#         return b  
      
#     return gcd(b%a, a)

# Second trail
#
# from collections import defaultdict
# def connectedCities(n, g, originCities, destinationCities):
#     # create a connectedness matrix
#     connectedness_matrix = [[0 for i in range(n+1)] for i in range(n+1)]
#     visited_nodes = defaultdict(bool)
#     for i in range(len(originCities)):
#         for j in range(len(destinationCities)):
#             if gcd(originCities[i], destinationCities[j]) > g:    
#                 connectedness_matrix[originCities[i]][destinationCities[j]] = 1
#                 connectedness_matrix[destinationCities[j]][originCities[i]] = 1

#     def bfs(a,b):
#         result = []
#         queue=[]
#         queue.append(a)
#         while queue:
#             node = queue.pop(0)
#             result.append(node)
#             if not visited_nodes[node]:
#                 visited_nodes[node] = True
#                 for i in range(n+1):
#                     if connectedness_matrix[node][i] == 1 and not visited_nodes[i]:
#                         queue.append(i)

#             if node == b:
#                 result.append(b)
#                 return result
#         return result

#     def bfs_cache(a,b):
#         if connectedness_matrix[a][b] == 1:
#             return 1
#         if visited_nodes[a] and visited_nodes[b]:
#             return 0
#         connected_nodes = bfs(a,b)
#         for i in range(len(connected_nodes)):
#             for j in range(len(connected_nodes)):
#                 connectedness_matrix[connected_nodes[i]][connected_nodes[j]] = 1
#                 connectedness_matrix[connected_nodes[j]][connected_nodes[i]] = 1
#         return connectedness_matrix[a][b]


#     result_list = []
#     for i in range(len(originCities)):
#         result = bfs_cache(originCities[i], destinationCities[i])
#         result_list.append(result)

#     return result_list