def zombieCluster(zombies):
    # Write your code here
    v = [[False for i in range(len(zombies))] for i in range(len(zombies))]
    
    counter=0
    for row in range(len(zombies)):
        for column in range(len(zombies)):
            bfs_result = bfs(zombies, v, row, column)
            if len(bfs_result) > 0:
                counter+=1
                      
    return counter

def bfs(zombies, visited, row, column):
    result_set = set()
    if not visited[row][column]:
        visited[row][column] = True
        queue = []
        if zombies[row][column] == '1':
            result_set.add(row)
            result_set.add(column)
            for i in range(len(zombies)):
                if zombies[i][column] == '1':
                    result_set.add(i)
                    result_set.add(column)
                    queue.append((i,column))
            for i in range(len(zombies)):
                if zombies[row][i] == '1':
                    result_set.add(i)
                    result_set.add(row)
                    queue.append((row,i))
            while queue:
                node = queue.pop(0)
                result_set.update(bfs(zombies, visited, node[0], node[1]))
    return result_set
        
                
            


print(zombieCluster(["1100","1110","0110","0001"])==2)
print(zombieCluster(["1000","0100","0010","0001"])==4)
print(zombieCluster(["1000","1100","0010","0001"])==3)
print(zombieCluster(["1010","1100","0010","0001"])==2)
print(zombieCluster(["1010","1100","0011","0001"])==1)
print(zombieCluster(["1001","0100","0010","0001"])==3)
print(zombieCluster(["1000","1100","1010","1001"])==1)
print(zombieCluster(["1111","0100","0010","0001"])==1)
print(zombieCluster(["10000","11000","01100","00110","00011"])==1)
print(zombieCluster(["10000","01000","01100","00110","00011"])==2)
print(zombieCluster(["10000","01000","00100","00110","00011"])==3)
print(zombieCluster(["10000","01000","00100","00010","00011"])==4)
print(zombieCluster(["10000","01000","00100","00011","00001"])==4)
print(zombieCluster(["10000","01000","00110","00011","00001"])==3)
print(zombieCluster(["10000","01100","00110","00011","00001"])==2)
print(zombieCluster(["11000","01100","00110","00011","00001"])==1)
print(zombieCluster(["10000","01010","00100","00010","00001"])==4)
print(zombieCluster(["11111","11111","11111","11111","11111"])==1)
print(zombieCluster(["11111","11101","11111","10111","11111"])==1)
print(zombieCluster(["11111","01111","00111","00011","00001"])==1)
print(zombieCluster(["1"])==1)
print(zombieCluster([])==0)
print(zombieCluster(["100","010","001"])==3)
print(zombieCluster(["100","111","001"])==1)
print(zombieCluster(["100","010","111"])==1)
print(zombieCluster(["100","010","101"])==2)
print(zombieCluster(["10111","01011","00101","00010","00001"])==1)

# def zombieCluster(zombies):
#     # Write your code here
#     zombie_dict = {}
#     v = [[False for i in range(len(zombies))] for i in range(len(zombies))]
    
#     for row in range(len(zombies)):
#         for column in range(len(zombies)):
#             bfs(zombies, v, zombie_dict, row, column)
                      
#     result_set = set()
#     for k,v in zombie_dict.items():
#         result_set.add(v)
#     return len(result_set)

# def bfs(zombies, visited, zombie_dict, row, column):
#     if not visited[row][column]:
#         visited[row][column] = True
#         queue = []
#         if zombies[row][column] == '1':
#             for i in range(row, len(zombies)):
#                 if zombies[i][column] == '1':
#                     if column in zombie_dict:
#                         zombie_dict[i] = zombie_dict[column]
#                     elif i in zombie_dict:
#                         zombie_dict[column] = zombie_dict[i]
#                     else:
#                         zombie_dict[row] = len(zombie_dict)
#                     queue.append((i,column))
#             for i in range(column, len(zombies)):
#                 if zombies[row][i] == '1':
#                     if row in zombie_dict:
#                         zombie_dict[i] = zombie_dict[row]
#                     elif i in zombie_dict:
#                         zombie_dict[row] = zombie_dict[i]
#                     else:
#                         zombie_dict[row] = len(zombie_dict)
#                     queue.append((row,i))
#             while queue:
#                 node = queue.pop(0)
#                 bfs(zombies, visited, zombie_dict, node[0], node[1])
