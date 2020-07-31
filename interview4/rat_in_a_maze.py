maze = [
"#################",
"#S  #       #   #",
"### ### ### # # #",
"# #   #   # # # #",
"# ### ### # # # #",
"#   #     # # # #",
"# # ####### ### #",
"# #       # #   #",
"# ### ### # # # #",
"#   # #       # #",
"# ### ######### #",
"# #   #     #   #",
"# # ### ### # ###",
"# #   # #   #   #",
"# ### # # ##### #",
"#   #   #     #E#",
"#################"]

def loc(maze, x, y):
    return maze[y][x]

def update(maze, x, y, val):
    maze[y] = maze[y][:x] + val + maze[y][x + 1:]

def print_maze(maze):
    print("\n")
    for line in maze:
        print(line)
    print("\n")

start = [1,1]

def solve_maze(maze):
    print_maze(maze)
    
    if solve_maze_util(maze, start):
        print_maze(maze)
    else:
        print("False")
    

def solve_maze_util(maze, start):
    x = start[0]
    y = start[1]
    
    # Find out the value at 4 different directions - [x+1, y], [x-1, y], [x, y+1], [x,y-1]
    
    # value is E
    if loc(maze, x, y) == 'E':
        return True
    
    update(maze, x, y, 'X')
    
    neighbors = [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]
    
    for nbr in neighbors:
        new_x = nbr[0]
        new_y = nbr[1]
        
    
        # Check one direction - down [x, y+1]
        if loc(maze, new_x, new_y) != '#' and loc(maze, new_x, new_y) != 'X':
            if not solve_maze_util(maze, [new_x, new_y]):
                # change the position
                update(maze, new_x, new_y, " ")
            else: 
                return True
    
    return False
    # If value is not equals '#', then take this position recurse
    
    
    
solve_maze(maze)