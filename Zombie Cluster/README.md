# Zombie Clusters

Company| Ascend.io
---|---
Date|11/12/2018
Platform|HackerRank

There are Zomies in Seattle. Liv and Ravi are trying to track them down to find out who is creating new zombies in an effort to prevent an apocalypse. Other than the patient-zero zombies (who became so by mixing Max Rager and tainted Utopoium), new people only become zombies after being scratched by an existing zombie. Zombiism is transitive. This means that if zombie 0 knows zombie 1 and zombie 1 knows zombie 2, then zombie 0 is connected to zombie 2 by way of knowing zombie 1. A zombie cluster is a group of zombies who are dicrectly or indirectly linked through the other zombies thy know, such as the one who scratched them or supplies who them brains with.

The diagram showing connectedness will be made up of a number of binary strings, characters 0 or 1. Each of the characters in the string respresents whether the zombie associcated with a row element is connected to the zombie at that characters's index. For instance, a zombie 0 with a connectedness string '110' is connected to zombies 0 (itself) and zombie 1, but not to zombie 2. The complete matrix of zombie connectedness is:

```
110
110
001
```
Zombies 0 and 1 are connected. Zombie 2 is not.

Your task is to determine the number of connected groups of zombies, or clusters, in a given matrix.

__Note__: Method signatures may vary depending on the requirements of your chosen language.

### Function Description
Comete the function _zombieCluster_ in the editor below. The function must return an integer representing the number of zombie clusters counted.

zombieCluster has the following parameter(s):
     _zombies[zombies[0],...zombies[n-1]]:_ an array of string of binary digits _z[i]_ repsensting connetedness of zombies
#### Constraints
* 1 <= n <= 300
* 0 <= i <= n
* |zombies| = n
* Each _zombies[i]_ contains a binary string of _n_ zeros and ones. It is a square matrix.

### Sample Case 0
#### Sample Input 0
```
4
1100
1110
0110
0001
```

#### Sample Output 0
```
2
```
In the diagram below, the squares highlighting a known connection between two differenct zombies are highlighted in green. Because each zombie is already aware that they are personllay a zombie, those are highlighted in grey.

![Explanation 0](/Explanation0.png)

We have n = 4 zombies numbered _z[0]_ through _z[3]_. There are 2 pairs of zombies who directly know each another: _(z[0],z[1])_ and _(z[1],z[2])_. Beause of zombiism's transitive property, the set of zombies _{z[0], z[1],z[2]}_ is considered to be a single zombie cluster. The remaining zombie, _z[3]_, doesn't know any other zombies and is considered to be hin own sperate zombie cluster({z[3]}). This gives us a total of 2 zombie clusters.

### Sample Case 1
#### Sample Input 1
```
5
10000
01000
00100
00010
00001
```
#### Sample Output 1
```
5
```

#### Explanation 1
In the diagram below, the squares highlighting a known connection between two different zombies are highlighted in green. Becuase each zombies is already aware that they are personally a zombie, those are highlighted in grey.
![Explanation 0](/Explanation1.png)
No zombie knows who any other zombie is, so they each form their own zombie cluster: _{z[0]},{z[1]},{z[2]},{z[3]} and {z[4]}}_. This means we have 5 zombie cuslters, so we print 5 on a new line.

### Solution
My first solution iterating over the matrix line by line and storing each hit of one in a map(dict) zombie_id->group_number isn't correct.

You need to do dfs or bfs otherwise you do not find the complete group in every case.

This is my solution now, but I am sure it can be written much more compact.

```
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
```
