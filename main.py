import RubikCube


def checkVisited(visited, cube):
    for i in visited:
        if cube.checkEqual(i):
            return True
    return False


def Neighbours(cube):
    b = RubikCube.RubikCube()
    b.copy(cube.rotateB())
    f = RubikCube.RubikCube()
    f.copy(cube.rotateF())
    d = RubikCube.RubikCube()
    d.copy(cube.rotateD())
    u = RubikCube.RubikCube()
    u.copy(cube.rotateU())
    l = RubikCube.RubikCube()
    l.copy(cube.rotateL())
    r = RubikCube.RubikCube()
    r.copy(cube.rotateR())
    return [f, b, u, d, l, r]


Cube = RubikCube.RubikCube()
Visited = []                                # List for visited
queue = []                                  # Initialize a queue

Cube = Cube.rotateR()                       # shuffling
Cube = Cube.rotateR()
Cube = Cube.rotateR()
Cube = Cube.rotateU()

Cube.Print()                                # Initial Print
print("\n\nSolved Cube:\n")


def bfs(visited, cube):                      # function for BFS start with given cube
    visited.append(cube)
    queue.append(cube)

    while queue:                             # Creating loop to visit each node
        m = queue.pop(0)

        for neighbour in Neighbours(m):      # Neighbours return a list of moves applied to m
            if neighbour.checkGoal():        # checks if solved
                neighbour.Print()
                return
            if not checkVisited(visited, neighbour):        # checks if already visited
                visited.append(neighbour)
                queue.append(neighbour)


bfs(Visited, Cube)