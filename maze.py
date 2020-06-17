import sys

if len(sys.argv) != 3:
    print("Read The 'Readme' file\n")
    # python maze.py fast maze.txt
else:
    filename=sys.argv[2]
    BFS = 0
    DFS = -1
    lookup = {"fast":DFS,
              "efficient":BFS}
    
    DATASTRUCTURE = lookup.get(sys.argv[1].lower())
    class MAZE:
        def __init__(self, filename):

            self.spaces = 0
            with open(filename) as f:
                contents = f.read()
            if contents.count("A") != 1:
                raise Exception("maze must have exactly one start point")
            if contents.count("B") != 1:
                raise Exception("maze must have exactly one goal")

            # Determine height and width of maze
            contents = contents.splitlines()
            self.height = len(contents)
            self.width = max(len(line) for line in contents)

            # Keep track of walls
            self.walls = []
            for i in range(self.height):
                row = []
                for j in range(self.width):
                    try:
                        if contents[i][j] == "A":
                            self.start = (i, j)
                            row.append(False)
                        elif contents[i][j] == "B":
                            self.goal = (i, j)
                            row.append(False)
                        elif contents[i][j] == " ":
                            self.spaces += 1
                            row.append(False)
                        else:
                            row.append(True)
                    except IndexError:
                        row.append(False)
                self.walls.append(row)

            self.solution = None

        def showdata(self):
            print(self.height,self.width)
            print(self.start)

        def IsConnected(self):
            row = self.node[0]
            col = self.node[1]
            direction = {
                    "LEFT": (row,col-1),
                    "UP": (row-1,col),
                    "RIGHT": (row,col+1),
                    "DOWN": (row+1,col)
                }
            lst = []
            for i in direction.values():
                r = i[0]
                c = i[1]
                if (0<=r<self.height and 0<=c<self.width) and self.walls[r][c] == False:
                    lst.append((r,c))
            return lst
                
            
            
        def BFS(self):
            
            self.visited = []
            self.visited.append(self.start)
            self.queue = []
            self.queue.append(self.start)
            self.path = []
            self.distance = []
            for i in range(self.height):
                self.path.append([0 for j in range(self.width)])
                self.distance.append([0 for j in range(self.width)])
            
            while(self.queue != [] and self.goal not in self.visited):
                self.node = self.queue.pop(DATASTRUCTURE)
                conn = MAZE.IsConnected(self)
                for i in range(len(conn)):
                    if conn[i] not in self.visited:
                        self.visited.append(conn[i])
                        self.queue.append((conn[i]))
                        self.distance[conn[i][0]] [conn[i][1]] = self.distance[self.node[0]][self.node[1]] + 1
                        r,c = self.node
                        self.path[conn[i][0]][conn[i][1]] = (r,c)
                        
            self.ans = []

            if self.distance[self.goal[0]][self.goal[1]] != 0:
                print("Shortest Distance Possible:",self.distance[self.goal[0]][self.goal[1]]-1)
                r,c = self.goal[0],self.goal[1]
                while((r,c) != self.start):
                    self.ans.append(self.path[r][c])
                    r,c = self.path[r][c]
                self.ans.pop(-1)

        def ANS(self):
            TGREEN = '\033[m'
            if self.ans == []:
                print("NO Solution Possible")
            else:
                for i in range(self.height):
                    for j in range(self.width):
                        if self.walls[i][j] == True:
                            print("█",end="")
                        if (i,j) == self.goal:
                            print("B",end="")
                        elif (i,j) == self.start:
                            print("A",end="")
                        elif (i,j) in self.ans:
                            print("*",end="")
                        elif self.walls[i][j] == False:
                            print(" ",end="")
                        
                    print()
            print("Total cells visited:",len(self.visited))
            print("Total Available Paths:",self.spaces)
    try:
        maze = MAZE(filename)
        maze.BFS()
        print()
        maze.ANS()
    except:
        print("Invalid File Name or Invalid Options")
    

        
