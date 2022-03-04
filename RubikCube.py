import copy


def deepCopy(destination, sour):
    for i in range(len(sour)):
        for j in range(len(sour[i])):
            destination[i][j] = sour[i][j]


def CheckEqual(array, sour):
    for i in range(len(sour)):
        for j in range(len(sour[i])):
            if array[i][j] != sour[i][j]:
                return False
    return True


class RubikCube:
    F = [[], [], []]
    R = [[], [], []]
    U = [[], [], []]
    D = [[], [], []]
    B = [[], [], []]
    L = [[], [], []]
    Moves = []

    def __init__(self):
        self.F = [['R', 'R', 'R'],
                  ['R', 'R', 'R'],
                  ['R', 'R', 'R']]
        self.R = [['B', 'B', 'B'],
                  ['B', 'B', 'B'],
                  ['B', 'B', 'B']]
        self.U = [['W', 'W', 'W'],
                  ['W', 'W', 'W'],
                  ['W', 'W', 'W']]
        self.D = [['Y', 'Y', 'Y'],
                  ['Y', 'Y', 'Y'],
                  ['Y', 'Y', 'Y']]
        self.B = [['O', 'O', 'O'],
                  ['O', 'O', 'O'],
                  ['O', 'O', 'O']]
        self.L = [['G', 'G', 'G'],
                  ['G', 'G', 'G'],
                  ['G', 'G', 'G']]
        self.Moves = []

    def copy(self, temp):
        deepCopy(self.F, temp.F)
        deepCopy(self.R, temp.R)
        deepCopy(self.B, temp.B)
        deepCopy(self.L, temp.L)
        deepCopy(self.U, temp.U)
        deepCopy(self.D, temp.D)

    def checkEqual(self, obj):
        return (CheckEqual(self.F, obj.F) and CheckEqual(self.L, obj.L) and CheckEqual(self.R,
                                                                                       obj.R) and CheckEqual(self.U,
                                                                                                             obj.U) and CheckEqual(
            self.D, obj.D) and CheckEqual(self.B, obj.B))

    def checkGoal(self):
        if self.F == [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']] and self.R == [['B', 'B', 'B'],
                                                                                        ['B', 'B', 'B'],
                                                                                        ['B', 'B', 'B']] and self.U == [
            ['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']] and self.D == [['Y', 'Y', 'Y'],
                                                                              ['Y', 'Y', 'Y'],
                                                                              ['Y', 'Y', 'Y']] and self.B == [
            ['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']
        ] and self.L == [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']]:
            return True
        return False

    def Print(self):
        print("            ", self.U[0][0], " ", self.U[0][1], " ", self.U[0][2])
        print("            ", self.U[1][0], " ", self.U[1][1], " ", self.U[1][2])
        print("            ", self.U[2][0], " ", self.U[2][1], " ", self.U[2][2])
        print("")
        print(self.L[0][0], " ", self.L[0][1], " ", self.L[0][2], "  ", self.F[0][0], " ", self.F[0][1], " ",
              self.F[0][2],
              "  ", self.R[0][0], " ", self.R[0][1],
              " ", self.R[0][2], "  ", self.B[0][0], " ", self.B[0][1],
              " ", self.B[0][2])
        print(self.L[1][0], " ", self.L[1][1], " ", self.L[1][2], "  ", self.F[1][0], " ", self.F[1][1], " ",
              self.F[1][2], "  ", self.R[1][0], " ", self.R[1][1],
              " ", self.R[1][2], "  ", self.B[1][0], " ", self.B[1][1],
              " ", self.B[1][2])
        print(self.L[2][0], " ", self.L[2][1], " ", self.L[2][2], "  ", self.F[2][0], " ", self.F[2][1], " ",
              self.F[2][2], "  ", self.R[2][0], " ", self.R[2][1],
              " ", self.R[2][2], "  ", self.B[2][0], " ", self.B[2][1],
              " ", self.B[2][2])
        print("")
        print("            ", self.D[0][0], " ", self.D[0][1], " ", self.D[0][2])
        print("            ", self.D[1][0], " ", self.D[1][1], " ", self.D[1][2])
        print("            ", self.D[2][0], " ", self.D[2][1], " ", self.D[2][2])

    # rotating clockwise------------------------------------------------
    def rotateF(self):
        c = copy.deepcopy(self)
        c.Moves.append("F")
        # Forward
        temp = c.F[0][0]
        c.F[0][2], temp = temp, c.F[0][2]
        c.F[2][2], temp = temp, c.F[2][2]
        c.F[2][0], temp = temp, c.F[2][0]
        c.F[0][0] = temp
        temp = c.F[0][1]
        c.F[1][2], temp = temp, c.F[1][2]
        c.F[2][1], temp = temp, c.F[2][1]
        c.F[1][0], temp = temp, c.F[1][0]
        c.F[0][1] = temp

        # Sides
        temp = c.U[2]
        c.R[0][0], temp[0] = temp[0], c.R[0][0]
        c.R[1][0], temp[1] = temp[1], c.R[1][0]
        c.R[2][0], temp[2] = temp[2], c.R[2][0]

        c.D[0][0], temp[2] = temp[2], c.D[0][0]
        c.D[0][1], temp[1] = temp[1], c.D[0][1]
        c.D[0][2], temp[0] = temp[0], c.D[0][2]

        c.L[0][2], temp[2] = temp[2], c.L[0][2]
        c.L[1][2], temp[1] = temp[1], c.L[1][2]
        c.L[2][2], temp[0] = temp[0], c.L[2][2]
        c.U[2] = temp
        return c

    def rotateL(self):
        c = copy.deepcopy(self)
        c.Moves.append("L")
        # Face
        temp = c.L[0][0]
        c.L[0][2], temp = temp, c.L[0][2]
        c.L[2][2], temp = temp, c.L[2][2]
        c.L[2][0], temp = temp, c.L[2][0]
        c.L[0][0] = temp
        temp = c.L[0][1]
        c.L[1][2], temp = temp, c.L[1][2]
        c.L[2][1], temp = temp, c.L[2][1]
        c.L[1][0], temp = temp, c.L[1][0]
        c.L[0][1] = temp

        # Sides
        temp0 = c.U[0][0]
        temp1 = c.U[1][0]
        temp2 = c.U[2][0]
        c.F[0][0], temp0 = temp0, c.F[0][0]
        c.F[1][0], temp1 = temp1, c.F[1][0]
        c.F[2][0], temp2 = temp2, c.F[2][0]
        c.D[0][0], temp0 = temp0, c.D[0][0]
        c.D[1][0], temp1 = temp1, c.D[1][0]
        c.D[2][0], temp2 = temp2, c.D[2][0]
        c.B[0][2], temp2 = temp2, c.B[0][2]
        c.B[1][2], temp1 = temp1, c.B[1][2]
        c.B[2][2], temp0 = temp0, c.B[2][2]
        c.U[0][0] = temp0
        c.U[1][0] = temp1
        c.U[2][0] = temp2
        return c

    def rotateR(self):
        c = copy.deepcopy(self)
        c.Moves.append("R")
        # Face
        temp = c.R[0][0]
        c.R[0][2], temp = temp, c.R[0][2]
        c.R[2][2], temp = temp, c.R[2][2]
        c.R[2][0], temp = temp, c.R[2][0]
        c.R[0][0] = temp
        temp = c.R[0][1]
        c.R[1][2], temp = temp, c.R[1][2]
        c.R[2][1], temp = temp, c.R[2][1]
        c.R[1][0], temp = temp, c.R[1][0]
        c.R[0][1] = temp

        # Sides
        temp0 = c.U[0][2]
        temp1 = c.U[1][2]
        temp2 = c.U[2][2]
        c.B[0][0], temp2 = temp2, c.B[0][0]
        c.B[1][0], temp1 = temp1, c.B[1][0]
        c.B[2][0], temp0 = temp0, c.B[2][0]
        c.D[0][2], temp0 = temp0, c.D[0][2]
        c.D[1][2], temp1 = temp1, c.D[1][2]
        c.D[2][2], temp2 = temp2, c.D[2][2]
        c.F[0][2], temp0 = temp0, c.F[0][2]
        c.F[1][2], temp1 = temp1, c.F[1][2]
        c.F[2][2], temp2 = temp2, c.F[2][2]
        c.U[0][2] = temp0
        c.U[1][2] = temp1
        c.U[2][2] = temp2
        return c

    def rotateU(self):
        c = copy.deepcopy(self)
        c.Moves.append("U")
        # Face
        temp = c.U[0][0]
        c.U[0][2], temp = temp, c.U[0][2]
        c.U[2][2], temp = temp, c.U[2][2]
        c.U[2][0], temp = temp, c.U[2][0]
        c.U[0][0] = temp
        temp = c.U[0][1]
        c.U[1][2], temp = temp, c.U[1][2]
        c.U[2][1], temp = temp, c.U[2][1]
        c.U[1][0], temp = temp, c.U[1][0]
        c.U[0][1] = temp

        # Sides
        temp = c.F[0]
        c.L[0], temp = temp, c.L[0]
        c.B[0], temp = temp, c.B[0]
        c.R[0], temp = temp, c.R[0]
        c.F[0] = temp
        return c

    def rotateD(self):
        c = copy.deepcopy(self)
        c.Moves.append("D")
        # Face
        temp = c.D[0][0]
        c.D[0][2], temp = temp, c.D[0][2]
        c.D[2][2], temp = temp, c.D[2][2]
        c.D[2][0], temp = temp, c.D[2][0]
        c.D[0][0] = temp
        temp = c.D[0][1]
        c.D[1][2], temp = temp, c.D[1][2]
        c.D[2][1], temp = temp, c.D[2][1]
        c.D[1][0], temp = temp, c.D[1][0]
        c.D[0][1] = temp

        # Sides
        temp = c.F[2]
        c.R[2], temp = temp, c.R[2]
        c.B[2], temp = temp, c.B[2]
        c.L[2], temp = temp, c.L[2]
        c.F[2] = temp
        return c

    def rotateB(self):
        c = copy.deepcopy(self)
        c.Moves.append("B")
        # Face
        temp = c.B[0][0]
        c.B[0][2], temp = temp, c.B[0][2]
        c.B[2][2], temp = temp, c.B[2][2]
        c.B[2][0], temp = temp, c.B[2][0]
        c.B[0][0] = temp
        temp = c.B[0][1]
        c.B[1][2], temp = temp, c.B[1][2]
        c.B[2][1], temp = temp, c.B[2][1]
        c.B[1][0], temp = temp, c.B[1][0]
        c.B[0][1] = temp

        # Sides
        temp = c.U[0]
        c.L[0][0], temp[0] = temp[0], c.L[0][0]
        c.L[1][0], temp[1] = temp[1], c.L[1][0]
        c.L[2][0], temp[2] = temp[2], c.L[2][0]

        c.D[2][0], temp[0] = temp[0], c.D[2][0]
        c.D[2][1], temp[1] = temp[1], c.D[2][1]
        c.D[2][2], temp[2] = temp[2], c.D[2][2]

        c.R[0][2], temp[0] = temp[0], c.R[0][2]
        c.R[1][2], temp[1] = temp[1], c.R[1][2]
        c.R[2][2], temp[2] = temp[2], c.R[2][2]
        c.U[0] = temp
        return c

# ------------------------End of File------------------------------
