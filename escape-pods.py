def ford_fulkerson(entrance, exit, path):
    from collections import deque
    n = len(path)
    maxFlow = 0
    while True:
        dq = deque([entrance])
        visited = set([entrance])
        parent = [-1 for _ in range(n)]
        flow = float('inf')
        while dq:
            u = dq.popleft()
            for v in range(n):
                if v not in visited and path[u][v] > 0:
                    dq.append(v)
                    visited.add(v)
                    parent[v] = u
                    flow = min(flow, path[u][v])

        # Break if can not find augmented path to exit
        if exit not in visited:
            break

        # Update maxFlow
        maxFlow += flow

        # Update graph
        v = exit
        while v != entrance:
            u = parent[v]
            path[u][v] -= flow
            path[v][u] += flow
            v = parent[v]

    return maxFlow


def solution(entrances, exits, path):
    # Modify graph to single entrance and single exit
    n = len(path)
    for i in range(len(path)):
        path[i] += [0, 0]
    path.append([0 for _ in range(n + 2)])
    path.append([0 for _ in range(n + 2)])

    # New entrance and new exit are the 2 last doors
    new_entrance = n
    new_exit = n + 1

    # Capacity from new_entrance to each entrance equals to capacity from that entrance
    for entrance in entrances:
        path[new_entrance][entrance] = sum(path[entrance])

    # Capacity from each exit to new_exit equals to capacity to that exit
    for exit in exits:
        path[exit][new_exit] = sum([path[_][exit] for _ in range(n)])

    return ford_fulkerson(new_entrance, new_exit, path)


if __name__ == '__main__':
    output = solution(entrances=[0],
                      exits=[3],
                      path=[[0, 7, 0, 0],
                            [0, 0, 6, 0],
                            [0, 0, 0, 8],
                            [0, 0, 0, 0]])

    output = solution(entrances=[0, 1],
                      exits=[4, 5],
                      path=[[0, 0, 4, 6, 0, 0],
                            [0, 0, 5, 2, 0, 0],
                            [0, 0, 0, 0, 4, 4],
                            [0, 0, 0, 0, 6, 6],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0]])

    print(output)


'''
Escape Pods

===========

You've blown up the LAMBCHOP doomsday device and relieved the bunnies of their work duries -- and now you need to escape from the space station as quickly and as orderly as possible! The bunnies have all gathered in various locations throughout the station, and need to make their way towards the seemingly endless amount of escape pods positioned in other parts of the station. You need to get the numerous bunnies through the various rooms to the escape pods. Unfortunately, the corridors between the rooms can only fit so many bunnies at a time. What's more, many of the corridors were resized to accommodate the LAMBCHOP, so they vary in how many bunnies can move through them at a time.

Given the starting room numbers of the groups of bunnies, the room numbers of the escape pods, and how many bunnies can fit through at a time in each direction of every corridor in between, figure out how many bunnies can safely make it to the escape pods at a time at peak.

Write a function solution(entrances, exits, path) that takes an array of integers denoting where the groups of gathered bunnies are, an array of integers denoting where the escape pods are located, and an array of an array of integers of the corridors, returning the total number of bunnies that can get through at each time step as an int. The entrances and exits are disjoint and thus will never overlap. The path element path[A][B] = C describes that the corridor going from A to B can fit C bunnies at each time step.  There are at most 50 rooms connected by the corridors and at most 2000000 bunnies that will fit at a time.

For example, if you have:

entrances = [0, 1]

exits = [4, 5]

path = [

[0, 0, 4, 6, 0, 0],  # Room 0: Bunnies

[0, 0, 5, 2, 0, 0],  # Room 1: Bunnies

[0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room

[0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room

[0, 0, 0, 0, 0, 0],  # Room 4: Escape pods

[0, 0, 0, 0, 0, 0],  # Room 5: Escape pods

]

Then in each time step, the following might happen:

0 sends 4/4 bunnies to 2 and 6/6 bunnies to 3

1 sends 4/5 bunnies to 2 and 2/2 bunnies to 3

2 sends 4/4 bunnies to 4 and 4/4 bunnies to 5

3 sends 4/6 bunnies to 4 and 4/6 bunnies to 5

So, in total, 16 bunnies could make it to the escape pods at 4 and 5 at each time step.  (Note that in this example, room 3 could have sent any variation of 8 bunnies to 4 and 5, such as 2/6 and 6/6, but the final solution remains the same.)

Languages

=========

To provide a Java solution, edit Solution.java

To provide a Python solution, edit solution.py

Test cases

==========

Your code should pass the following test cases.

Note that it may also be run against hidden test cases not shown here.

- - Java cases --

Input:

Solution.solution({0, 1}, {4, 5}, {{0, 0, 4, 6, 0, 0}, {0, 0, 5, 2, 0, 0}, {0, 0, 0, 0, 4, 4}, {0, 0, 0, 0, 6, 6}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}})

Output:

16

Input:

Solution.solution({0}, {3}, {{0, 7, 0, 0}, {0, 0, 6, 0}, {0, 0, 0, 8}, {9, 0, 0, 0}})

Output:

6

- - Python cases --

Input:

solution.solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]])

Output:

6

Input:

solution.solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])

Output:

16

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
'''