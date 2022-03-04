import copy
import RubikCube


def checkVisited(visited, cube):
    for i in visited:
        if cube.checkEqual(i):
            return True
    return False


def Neighbours(cube):
    b = copy.deepcopy(cube.rotateB())
    f = copy.deepcopy(cube.rotateF())
    d = copy.deepcopy(cube.rotateD())
    u = copy.deepcopy(cube.rotateU())
    left = copy.deepcopy(cube.rotateL())
    r = copy.deepcopy(cube.rotateR())
    return [f, b, u, d, left, r]


def bfs(visited, cube):  # function for BFS start with given cube
    visited.append(cube)
    queue.append(cube)

    while queue:  # Creating loop to visit each node
        m = queue.pop(0)
        for neighbour in Neighbours(m):  # Neighbours return a list of moves applied to m
            if neighbour.checkGoal():  # checks if solved
                return neighbour  # returns solved cube
            if not checkVisited(visited, neighbour):  # checks if already visited
                visited.append(neighbour)
                queue.append(neighbour)


def ApplyMove(cube, char):
    if char == "F":
        return cube.rotateF()
    elif char == "R":
        return cube.rotateR()
    elif char == "L":
        return cube.rotateL()
    elif char == "U":
        return cube.rotateU()
    elif char == "D":
        return cube.rotateD()
    elif char == "B":
        return cube.rotateB()


def StepWiseSolution(initial, moves):
    cube = copy.deepcopy(initial)
    print("Initially:\n")
    cube.Print()
    i = 1
    for char in moves:
        print("\nStep " + str(i) + ". Rotate " + str(char) + " Face:\n")
        cube = ApplyMove(cube, char)
        cube.Print()
        i = i + 1
    print("You have solved the Rubik Cube!\n")


Cube = RubikCube.RubikCube()
Visited = []  # List for visited
queue = []  # Initialize a queue
backtrack = []  # backtracking

Cube = Cube.rotateR()  # shuffling
Cube = Cube.rotateR()
Cube = Cube.rotateR()
Cube = Cube.rotateU()
Cube.Moves = []

print("Initial Cube:\n")
Cube.Print()  # Initial Print
print("\n\nSolved Cube:\n")

SolvedCube = copy.deepcopy(bfs(Visited, Cube))
SolvedCube.Print()

print("\n\nNow Showing Step-wise Solution:\n")
StepWiseSolution(Cube, SolvedCube.Moves)

