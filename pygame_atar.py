# import pygame
# import heapq

# # ตั้งค่าขนาดของกริด
# GRID_SIZE = 20
# CELL_SIZE = 30
# SCREEN_SIZE = GRID_SIZE * CELL_SIZE

# # สี
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)

# # ตั้งค่า Pygame
# pygame.init()
# screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
# pygame.display.set_caption("A* Pathfinding Game")
# clock = pygame.time.Clock()

# # สร้างกริด
# grid = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
# start = (0, 0)
# goal = (GRID_SIZE - 1, GRID_SIZE - 1)
# grid[start[0]][start[1]] = "S"
# grid[goal[0]][goal[1]] = "G"
# obstacles = []


# # ฟังก์ชัน heuristic (Manhattan Distance)
# def heuristic(a, b):
#     return abs(a[0] - b[0]) + abs(a[1] - b[1])


# # ฟังก์ชัน A* algorithm
# def astar(start, goal, grid):
#     open_list = []
#     heapq.heappush(open_list, (0, start))
#     came_from = {}
#     g_score = {start: 0}
#     f_score = {start: heuristic(start, goal)}

#     while open_list:
#         current = heapq.heappop(open_list)[1]

#         if current == goal:
#             path = []
#             while current in came_from:
#                 path.append(current)
#                 current = came_from[current]
#             path.append(start)
#             path.reverse()
#             return path

#         for neighbor in get_neighbors(current, grid):
#             tentative_g_score = g_score[current] + 1

#             if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
#                 came_from[neighbor] = current
#                 g_score[neighbor] = tentative_g_score
#                 f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
#                 if neighbor not in [i[1] for i in open_list]:
#                     heapq.heappush(open_list, (f_score[neighbor], neighbor))

#     return None


# # ฟังก์ชันหาเพื่อนบ้าน
# def get_neighbors(node, grid):
#     neighbors = []
#     for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#         x, y = node[0] + dx, node[1] + dy
#         if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != "X":
#             neighbors.append((x, y))
#     return neighbors


# # ฟังก์ชันวาดกริด
# def draw_grid():
#     for y in range(GRID_SIZE):
#         for x in range(GRID_SIZE):
#             color = WHITE
#             if grid[y][x] == "X":
#                 color = BLACK
#             elif grid[y][x] == "S":
#                 color = GREEN
#             elif grid[y][x] == "G":
#                 color = RED
#             elif grid[y][x] == "*":
#                 color = BLUE
#             pygame.draw.rect(
#                 screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
#             )
#             pygame.draw.rect(
#                 screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1
#             )


# # ฟังก์ชันหลัก
# def main():
#     running = True
#     path = None

#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 x, y = event.pos
#                 x //= CELL_SIZE
#                 y //= CELL_SIZE
#                 if grid[y][x] == ".":
#                     grid[y][x] = "X"
#                     obstacles.append((y, x))
#                 elif grid[y][x] == "X":
#                     grid[y][x] = "."
#                     obstacles.remove((y, x))
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     path = astar(start, goal, grid)
#                     if path:
#                         for step in path:
#                             if step != start and step != goal:
#                                 grid[step[0]][step[1]] = "*"

#         screen.fill(WHITE)
#         draw_grid()
#         pygame.display.flip()
#         clock.tick(30)

#     pygame.quit()


# if __name__ == "__main__":
#     main()


# import pygame
# import heapq

# # ตั้งค่าขนาดของกริด
# GRID_SIZE = 20
# CELL_SIZE = 30
# SCREEN_SIZE = GRID_SIZE * CELL_SIZE

# # สี
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)

# # ตั้งค่า Pygame
# pygame.init()
# screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
# pygame.display.set_caption("A* Pathfinding Game")
# clock = pygame.time.Clock()

# # สร้างกริด
# grid = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
# start = (0, 0)
# goal = (GRID_SIZE - 1, GRID_SIZE - 1)
# grid[start[0]][start[1]] = "S"
# grid[goal[0]][goal[1]] = "G"
# obstacles = []


# # ฟังก์ชัน heuristic (Manhattan Distance)
# def heuristic(a, b):
#     return abs(a[0] - b[0]) + abs(a[1] - b[1])


# # ฟังก์ชัน A* algorithm
# def astar(start, goal, grid):
#     open_list = []
#     heapq.heappush(open_list, (0, start))
#     came_from = {}
#     g_score = {start: 0}
#     f_score = {start: heuristic(start, goal)}

#     while open_list:
#         current = heapq.heappop(open_list)[1]

#         if current == goal:
#             path = []
#             while current in came_from:
#                 path.append(current)
#                 current = came_from[current]
#             path.append(start)
#             path.reverse()
#             return path

#         for neighbor in get_neighbors(current, grid):
#             tentative_g_score = g_score[current] + 1

#             if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
#                 came_from[neighbor] = current
#                 g_score[neighbor] = tentative_g_score
#                 f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
#                 if neighbor not in [i[1] for i in open_list]:
#                     heapq.heappush(open_list, (f_score[neighbor], neighbor))

#     return None


# # ฟังก์ชันหาเพื่อนบ้าน
# def get_neighbors(node, grid):
#     neighbors = []
#     for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#         x, y = node[0] + dx, node[1] + dy
#         if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != "X":
#             neighbors.append((x, y))
#     return neighbors


# # ฟังก์ชันวาดกริด
# def draw_grid():
#     for y in range(GRID_SIZE):
#         for x in range(GRID_SIZE):
#             color = WHITE
#             if grid[y][x] == "X":
#                 color = BLACK
#             elif grid[y][x] == "S":
#                 color = GREEN
#             elif grid[y][x] == "G":
#                 color = RED
#             elif grid[y][x] == "*":
#                 color = BLUE
#             pygame.draw.rect(
#                 screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
#             )
#             pygame.draw.rect(
#                 screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1
#             )


# # ฟังก์ชันหลัก
# def main():
#     running = True
#     path = None

#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 x, y = event.pos
#                 x //= CELL_SIZE
#                 y //= CELL_SIZE
#                 if grid[y][x] == ".":
#                     grid[y][x] = "X"
#                     obstacles.append((y, x))
#                 elif grid[y][x] == "X":
#                     grid[y][x] = "."
#                     obstacles.remove((y, x))
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     path = astar(start, goal, grid)
#                     if path:
#                         for step in path:
#                             if step != start and step != goal:
#                                 grid[step[0]][step[1]] = "*"

#         screen.fill(WHITE)
#         draw_grid()
#         pygame.display.flip()
#         clock.tick(30)

#     pygame.quit()


# if __name__ == "__main__":
#     main()


# import pygame
# import heapq
# import random

# # ตั้งค่าขนาดของกริด
# GRID_SIZE = 20
# CELL_SIZE = 30
# SCREEN_SIZE = GRID_SIZE * CELL_SIZE

# # สี
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)

# # ตั้งค่า Pygame
# pygame.init()
# screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
# pygame.display.set_caption("A* Pathfinding Game")
# clock = pygame.time.Clock()

# # สร้างกริด
# grid = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
# start = (0, 0)
# goal = (GRID_SIZE - 1, GRID_SIZE - 1)
# grid[start[0]][start[1]] = "S"
# grid[goal[0]][goal[1]] = "G"
# obstacles = []
# moving_obstacles = []


# # ฟังก์ชัน heuristic (Manhattan Distance)
# def heuristic(a, b):
#     return abs(a[0] - b[0]) + abs(a[1] - b[1])


# # ฟังก์ชัน A* algorithm
# def astar(start, goal, grid):
#     open_list = []
#     heapq.heappush(open_list, (0, start))
#     came_from = {}
#     g_score = {start: 0}
#     f_score = {start: heuristic(start, goal)}

#     while open_list:
#         current = heapq.heappop(open_list)[1]

#         if current == goal:
#             path = []
#             while current in came_from:
#                 path.append(current)
#                 current = came_from[current]
#             path.append(start)
#             path.reverse()
#             return path

#         for neighbor in get_neighbors(current, grid):
#             tentative_g_score = g_score[current] + 1

#             if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
#                 came_from[neighbor] = current
#                 g_score[neighbor] = tentative_g_score
#                 f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
#                 if neighbor not in [i[1] for i in open_list]:
#                     heapq.heappush(open_list, (f_score[neighbor], neighbor))

#     return None


# # ฟังก์ชันหาเพื่อนบ้าน
# def get_neighbors(node, grid):
#     neighbors = []
#     for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#         x, y = node[0] + dx, node[1] + dy
#         if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != "X":
#             neighbors.append((x, y))
#     return neighbors


# # ฟังก์ชันวาดกริด
# def draw_grid():
#     for y in range(GRID_SIZE):
#         for x in range(GRID_SIZE):
#             color = WHITE
#             if grid[y][x] == "X":
#                 color = BLACK
#             elif grid[y][x] == "S":
#                 color = GREEN
#             elif grid[y][x] == "G":
#                 color = RED
#             elif grid[y][x] == "*":
#                 color = BLUE
#             elif grid[y][x] == "M":
#                 color = YELLOW
#             pygame.draw.rect(
#                 screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
#             )
#             pygame.draw.rect(
#                 screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1
#             )


# # ฟังก์ชันสุ่มอุปสรรคเคลื่อนไหว
# def add_random_moving_obstacles():
#     for _ in range(4):
#         while True:
#             x = random.randint(0, GRID_SIZE - 1)
#             y = random.randint(0, GRID_SIZE - 1)
#             if grid[y][x] == ".":
#                 grid[y][x] = "M"
#                 moving_obstacles.append((y, x))
#                 break


# # ฟังก์ชันเคลื่อนที่อุปสรรค
# def move_obstacles():
#     for i, (y, x) in enumerate(moving_obstacles):
#         grid[y][x] = "."
#         while True:
#             new_x = x + random.choice([-1, 1, 0, 0])
#             new_y = y + random.choice([0, 0, -1, 1])
#             if (
#                 0 <= new_x < GRID_SIZE
#                 and 0 <= new_y < GRID_SIZE
#                 and grid[new_y][new_x] == "."
#             ):
#                 grid[new_y][new_x] = "M"
#                 moving_obstacles[i] = (new_y, new_x)
#                 break


# # ฟังก์ชันหลัก
# def main():
#     running = True
#     path = None
#     add_random_moving_obstacles()

#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 x, y = event.pos
#                 x //= CELL_SIZE
#                 y //= CELL_SIZE
#                 if grid[y][x] == ".":
#                     grid[y][x] = "X"
#                     obstacles.append((y, x))
#                 elif grid[y][x] == "X":
#                     grid[y][x] = "."
#                     obstacles.remove((y, x))
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     path = astar(start, goal, grid)
#                     if path:
#                         for step in path:
#                             if step != start and step != goal:
#                                 grid[step[0]][step[1]] = "*"

#         move_obstacles()
#         screen.fill(WHITE)
#         draw_grid()
#         pygame.display.flip()
#         clock.tick(30)

#     pygame.quit()


# if __name__ == "__main__":
#     main()


# import pygame
# import heapq
# import random

# # ตั้งค่าขนาดของกริด
# GRID_SIZE = 20
# CELL_SIZE = 30
# SCREEN_SIZE = GRID_SIZE * CELL_SIZE

# # สี
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)

# # ตั้งค่า Pygame
# pygame.init()
# screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
# pygame.display.set_caption("A* Pathfinding Game")
# clock = pygame.time.Clock()

# # สร้างกริด
# grid = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
# start = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
# goal = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
# grid[start[0]][start[1]] = "S"
# grid[goal[0]][goal[1]] = "G"
# obstacles = []
# moving_obstacles = []


# # สร้างอุปสรรคสีดำ
# def add_random_obstacles():
#     for _ in range(GRID_SIZE // 2):
#         while True:
#             x = random.randint(0, GRID_SIZE - 1)
#             y = random.randint(0, GRID_SIZE - 1)
#             if grid[y][x] == ".":
#                 grid[y][x] = "X"
#                 obstacles.append((y, x))
#                 break


# # ฟังก์ชัน heuristic (Manhattan Distance)
# def heuristic(a, b):
#     return abs(a[0] - b[0]) + abs(a[1] - b[1])


# # ฟังก์ชัน A* algorithm
# def astar(start, goal, grid):
#     open_list = []
#     heapq.heappush(open_list, (0, start))
#     came_from = {}
#     g_score = {start: 0}
#     f_score = {start: heuristic(start, goal)}

#     while open_list:
#         current = heapq.heappop(open_list)[1]

#         if current == goal:
#             path = []
#             while current in came_from:
#                 path.append(current)
#                 current = came_from[current]
#             path.append(start)
#             path.reverse()
#             return path

#         for neighbor in get_neighbors(current, grid):
#             tentative_g_score = g_score[current] + 1

#             if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
#                 came_from[neighbor] = current
#                 g_score[neighbor] = tentative_g_score
#                 f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
#                 if neighbor not in [i[1] for i in open_list]:
#                     heapq.heappush(open_list, (f_score[neighbor], neighbor))

#     return None


# # ฟังก์ชันหาเพื่อนบ้าน
# def get_neighbors(node, grid):
#     neighbors = []
#     for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#         x, y = node[0] + dx, node[1] + dy
#         if (
#             0 <= x < len(grid)
#             and 0 <= y < len(grid[0])
#             and grid[x][y] != "X"
#             and grid[x][y] != "M"
#         ):
#             neighbors.append((x, y))
#     return neighbors


# # ฟังก์ชันวาดกริด
# def draw_grid():
#     for y in range(GRID_SIZE):
#         for x in range(GRID_SIZE):
#             color = WHITE
#             if grid[y][x] == "X":
#                 color = BLACK
#             elif grid[y][x] == "S":
#                 color = GREEN
#             elif grid[y][x] == "G":
#                 color = RED
#             elif grid[y][x] == "*":
#                 color = BLUE
#             elif grid[y][x] == "M":
#                 color = YELLOW
#             pygame.draw.rect(
#                 screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
#             )
#             pygame.draw.rect(
#                 screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1
#             )


# # ฟังก์ชันสุ่มอุปสรรคเคลื่อนไหว
# def add_random_moving_obstacles():
#     for _ in range(4):
#         while True:
#             x = random.randint(0, GRID_SIZE - 1)
#             y = random.randint(0, GRID_SIZE - 1)
#             if grid[y][x] == ".":
#                 grid[y][x] = "M"
#                 moving_obstacles.append((y, x))
#                 break


# # ฟังก์ชันเคลื่อนที่อุปสรรค
# def move_obstacles():
#     for i, (y, x) in enumerate(moving_obstacles):
#         grid[y][x] = "."
#         while True:
#             new_x = x + random.choice([-1, 1, 0, 0])
#             new_y = y + random.choice([0, 0, -1, 1])
#             if (
#                 0 <= new_x < GRID_SIZE
#                 and 0 <= new_y < GRID_SIZE
#                 and grid[new_y][new_x] == "."
#                 and (new_y, new_x) != start
#             ):
#                 grid[new_y][new_x] = "M"
#                 moving_obstacles[i] = (new_y, new_x)
#                 break


# # ฟังก์ชันหลัก
# def main():
#     running = True
#     path = None
#     add_random_obstacles()
#     add_random_moving_obstacles()

#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 x, y = event.pos
#                 x //= CELL_SIZE
#                 y //= CELL_SIZE
#                 if grid[y][x] == ".":
#                     grid[y][x] = "X"
#                     obstacles.append((y, x))
#                 elif grid[y][x] == "X":
#                     grid[y][x] = "."
#                     obstacles.remove((y, x))
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     path = astar(start, goal, grid)
#                     if path:
#                         for step in path:
#                             if step != start and step != goal:
#                                 grid[step[0]][step[1]] = "*"

#         move_obstacles()
#         screen.fill(WHITE)
#         draw_grid()
#         pygame.display.flip()
#         clock.tick(30)

#     pygame.quit()


# if __name__ == "__main__":
#     main()


import pygame
import heapq
import random

# ตั้งค่าขนาดของกริด
GRID_SIZE = 20
CELL_SIZE = 30
SCREEN_SIZE = GRID_SIZE * CELL_SIZE

# สี
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# ตั้งค่า Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("A* Pathfinding Game")
clock = pygame.time.Clock()

# สร้างกริด
grid = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
start = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
goal = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
grid[start[0]][start[1]] = "S"
grid[goal[0]][goal[1]] = "G"
obstacles = []
moving_obstacles = []


# สร้างอุปสรรคสีดำ
def add_random_obstacles():
    num_obstacles = GRID_SIZE * 2  # เพิ่มจำนวนอุปสรรค
    for _ in range(num_obstacles):
        while True:
            x = random.randint(0, GRID_SIZE - 1)
            y = random.randint(0, GRID_SIZE - 1)
            if grid[y][x] == ".":
                grid[y][x] = "X"
                obstacles.append((y, x))
                break


# ฟังก์ชัน heuristic (Manhattan Distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# ฟังก์ชัน A* algorithm
def astar(start, goal, grid):
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for neighbor in get_neighbors(current, grid):
            tentative_g_score = g_score[current] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                if neighbor not in [i[1] for i in open_list]:
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None


# ฟังก์ชันหาเพื่อนบ้าน
def get_neighbors(node, grid):
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = node[0] + dx, node[1] + dy
        if (
            0 <= x < len(grid)
            and 0 <= y < len(grid[0])
            and grid[x][y] != "X"
            and grid[x][y] != "M"
        ):
            neighbors.append((x, y))
    return neighbors


# ฟังก์ชันวาดกริด
def draw_grid():
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            color = WHITE
            if grid[y][x] == "X":
                color = BLACK
            elif grid[y][x] == "S":
                color = GREEN
            elif grid[y][x] == "G":
                color = RED
            elif grid[y][x] == "*":
                color = BLUE
            elif grid[y][x] == "M":
                color = YELLOW
            pygame.draw.rect(
                screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )
            pygame.draw.rect(
                screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1
            )


# ฟังก์ชันสุ่มอุปสรรคเคลื่อนไหว
def add_random_moving_obstacles():
    for _ in range(4):
        while True:
            x = random.randint(0, GRID_SIZE - 1)
            y = random.randint(0, GRID_SIZE - 1)
            if grid[y][x] == ".":
                grid[y][x] = "M"
                moving_obstacles.append((y, x))
                break


# ฟังก์ชันเคลื่อนที่อุปสรรค
def move_obstacles():
    for i, (y, x) in enumerate(moving_obstacles):
        grid[y][x] = "."
        while True:
            new_x = x + random.choice([-1, 1, 0, 0])
            new_y = y + random.choice([0, 0, -1, 1])
            if (
                0 <= new_x < GRID_SIZE
                and 0 <= new_y < GRID_SIZE
                and grid[new_y][new_x] == "."
                and (new_y, new_x) != start
            ):
                grid[new_y][new_x] = "M"
                moving_obstacles[i] = (new_y, new_x)
                break


# ฟังก์ชันหลัก
def main():
    running = True
    path = None
    add_random_obstacles()
    add_random_moving_obstacles()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x //= CELL_SIZE
                y //= CELL_SIZE
                if grid[y][x] == ".":
                    grid[y][x] = "X"
                    obstacles.append((y, x))
                elif grid[y][x] == "X":
                    grid[y][x] = "."
                    obstacles.remove((y, x))
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    path = astar(start, goal, grid)
                    if path:
                        for step in path:
                            if step != start and step != goal:
                                grid[step[0]][step[1]] = "*"

        move_obstacles()
        screen.fill(WHITE)
        draw_grid()
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
