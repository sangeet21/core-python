from heapq import heappop, heappush


def heuristic(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def min_moves(grid, source, destination, move_rule):
    m, n = len(grid), len(grid[0])
    directions = [
        (move_rule[0], move_rule[1]),
        (move_rule[1], -move_rule[0]),
        (-move_rule[1], move_rule[0]),
        (-move_rule[0], -move_rule[1])
    ]
    def is_valid(x, y):
        return 0 <= x < m and 0 <= y < n and grid[x][y] == 0
    
    pq = [(0, source[0], source[1])]  
    visited = set()
    visited.add((source[0], source[1]))
    
    while pq:
        moves, x, y = heappop(pq)
        
        if (x, y) == (destination[0], destination[1]):
            return moves
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                estimated_cost = moves + 1 + heuristic(nx, ny, destination[0], destination[1])
                heappush(pq, (estimated_cost, nx, ny))
    
    return 0


grid = [
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0]
]
source = (1, 0)
destination = (5, 3)
move_rule = (1, 2)

print(min_moves(grid, source, destination, move_rule)) 
