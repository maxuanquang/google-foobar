def solution(grid):
    # Your code here
    from collections import deque
    m, n = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def bfs(grid):
        dq = deque([(0, 0, 1)])
        visited = set([(0, 0)])
        found = False
        shortest_path_length = m * n
        while len(dq) > 0:
            x, y, path_length = dq.popleft()
            if x == m - 1 and y == n - 1:
                found = True
                shortest_path_length = path_length
                break
            for dx, dy in directions:
                nei_x, nei_y = x + dx, y + dy
                if 0 <= nei_x < m and 0 <= nei_y < n and (nei_x, nei_y) not in visited and grid[nei_x][nei_y] == 0:
                    dq.append((nei_x, nei_y, path_length + 1))
                    visited.add((nei_x, nei_y))
        return found, shortest_path_length
    
    lengths = []
    # Default case - remove 0 wall
    found, path_length = bfs(grid)
    if found:
        if path_length == m + n - 1:
            return path_length
        lengths.append(path_length)
    # Cases when remove 1 wall
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                grid[i][j] = 0
                found, path_length = bfs(grid)
                if found:
                    if path_length == m + n - 1:
                        return path_length
                    lengths.append(path_length)
                grid[i][j] = 1
    return min(lengths)


if __name__ == '__main__':
    # input = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
    input = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
    output = solution(input)
    print(output)