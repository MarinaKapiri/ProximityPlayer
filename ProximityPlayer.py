class Cell:
    def __init__(self, value=0, owner=0):
        # Initialize the cell with a value and an owner
        self.value = value
        self.owner = owner

    def getValue(self):
        # Return the current value of the cell
        return self.value

    def setValue(self, value):
        # Set a new value for the cell
        self.value = value

    def getOwner(self):
        # Return the owner of the cell
        return self.owner

    def setOwner(self, owner):
        # Set a new owner for the cell
        self.owner = owner


class Proximity1:
    # Define an empty list to represent the cells
    CellList = []

    def __init__(self, pid, length_X=0, length_Y=0):
        # Initialize the player ID and board dimensions
        self.pid = pid
        self.length_X = length_X
        self.length_Y = length_Y

    def setPid(self, pid):
        # Set the player ID
        self.pid = pid

    def setBoardSize(self, length_X, length_Y):
        # Set the dimensions of the board
        self.length_X = length_X
        self.length_Y = length_Y

    def getPlayerName(self):
        # Return the names of the players in the group
        return "Marina"

    def findNeighbours(self, CellList):
        # Update the owner of neighboring cells if they are empty
        for i in range(self.length_X * self.length_Y):
            if CellList[i].value != 0:
                neighbours = self.findMyNeighbours(i)
                for j in neighbours:
                    if CellList[j].owner == 0:
                         CellList[j].owner = self.pid
        return CellList

    def placeTile(self, m, CellList):
        # Place a tile on the board in the most suitable position
        C = []
        score = []
        position = []
        defense = []
        downturn = []
        post3 = []
        post4 = []
        CellList = self.findNeighbours(CellList)
        score1 = 0
        score2 = 0
        for i in range(self.length_X * self.length_Y):
            C.append(CellList[i].value)
        c = sum(C)
        for i in range(self.length_X * self.length_Y):
            if c == 0:
                # If the board is empty, place the tile in the middle
                return ((self.length_X * self.length_Y) // 2 + (self.length_X // 2))
            elif CellList[i].value == 0 and CellList[i].owner == self.pid:
                neighbours1 = self.findMyNeighbours(i)
                for j in neighbours1:
                    if CellList[j].owner == self.pid and CellList[j].value != 0:
                        score1 += 1
                    elif CellList[j].owner != self.pid and CellList[j].value < m and CellList[j].value != 0:
                        score2 += CellList[j].value
                defense.append(score1)
                downturn.append(score2)
                total = score1 + score2
                score.append(total)
                score1 = 0
                score2 = 0
                position.append(i)
        post1 = max(score)
        times = score.count(post1)
        if times > 1:
            v = 1
            b = -1
            while v <= times:
                b = score.index(post1, b + 1)
                post4.append(b)
                post3.append(downturn[b])
                v += 1
            post5 = post3.index(max(post3))
            return position[post4[post5]]
        else:
            return position[score.index(post1)]

    def findMyNeighbours(self, k):
        # Find the neighbours of a cell at position k
        x = k // self.length_X
        y = k % self.length_X

        if x == 0 and y == 0:
            neighbours = [1, self.length_X]
            return neighbours
        if x == 0 and y == self.length_X - 1:
            neighbours = [k - 1, k + self.length_X, k + self.length_X - 1]
            return neighbours
        if x == self.length_Y - 1 and y == 0:
            neighbours = [k - self.length_X, k - self.length_X + 1, k + 1]
            return neighbours
        if x == self.length_Y - 1 and y == self.length_X - 1:
            neighbours = [k - self.length_X, k - 1]
            return neighbours
        if x == 0 and y > 0 and y < self.length_X - 1:
            neighbours = [k - 1, k + 1, k + self.length_X - 1, k + self.length_X]
            return neighbours
        if x == self.length_Y - 1 and y > 0 and y < self.length_X - 1:
            neighbours = [k - self.length_X, k - self.length_X + 1, k - 1, k + 1]
            return neighbours
        if x % 2 == 0 and y == 0:
            neighbours = [k + 1, k - self.length_X, k + self.length_X]
            return neighbours
        if x % 2 != 0 and y == 0:
            neighbours = [k + 1, k - self.length_X, k - self.length_X + 1, k + self.length_X, k + self.length_X + 1]
            return neighbours
        if x % 2 == 0 and y == self.length_X - 1:
            neighbours = [k - 1, k - self.length_X, k - self.length_X - 1, k + self.length_X - 1, k + self.length_X]
            return neighbours
        if x % 2 != 0 and y == self.length_X - 1:
            neighbours = [k - 1, k - self.length_X, k + self.length_X]
            return neighbours
        if x % 2 != 0 and y > 0 and y < self.length_X - 1:
            neighbours = [k - 1, k + 1, k - self.length_X, k - self.length_X + 1, k + self.length_X, k + self.length_X + 1]
            return neighbours
        if x % 2 == 0 and y > 0 and y < self.length_X - 1:
            neighbours = [k - 1, k + 1, k - self.length_X - 1, k - self.length_X, k + self.length_X - 1, k + self.length_X]
            return neighbours

    def applyChanges(self, m: int, CellList):
        # Apply changes to the board after placing a tile
        n = self.placeTile(m, CellList)
        CellList[n].value = m
        CellList[n].owner = self.pid
        for i in self.findMyNeighbours(n):
            if CellList[i].owner == self.pid and CellList[i].value != 0:
                CellList[i].value += 1
            elif CellList[i].value < m and CellList[i].owner != self.pid:
                CellList[i].owner = self.pid
        for i in range(self.length_X * self.length_Y):
            if CellList[i].value == 0 and CellList[i].owner == self.pid:
                CellList[i].owner = 0
        return CellList


if __name__ == '__main__':
    # Test the Cell class
    a = Cell()
    print(a.getValue(), a.getOwner())
    print()
    a.setValue(10)
    a.setOwner(2)
    print(a.getValue(), a.getOwner())

    print()
    print('*' * 15)
    print()

    # Initialize a list of cells to represent the board
    CellList = [Cell(0, 0), Cell(0, 0),
                Cell(0, 0), Cell(0, 0),
                Cell(0, 0), Cell(0, 0),
                Cell(0, 0), Cell(0, 0),
                Cell(0, 0), Cell(0, 0),
                Cell(0, 0), Cell(0, 0),
                Cell(0, 0), Cell(0, 0),
                Cell(0, 0), Cell(0, 0),
                Cell(0, 0), Cell(0, 0),
                Cell(0, 0), Cell(0, 0),
                Cell(0, 0), Cell(0, 0),
                Cell(0, 0), Cell(0, 0),
    ]

    # Test the Proximity1 class
    p = Proximity1(1, 6, 4)
    p.setPid(1)
    p.setBoardSize(6, 4)

    print()
    print('*' * 15)
    print()
    print(p.getPlayerName())

    print()
    print('*' * 15)
    print()
    CellList2 = p.findNeighbours(CellList)
    for i in range(24):
        print('cell(', CellList[i].value, ',', CellList[i].owner, ')')

    print()
    print('*' * 15)
    print()
    w = p.placeTile(10, CellList)
    print(w)

    print()
    print('*' * 15)
    print()
    print(p.findMyNeighbours(0))

    print()
    print('*' * 15)
    print()
    CellList2 = p.applyChanges(10, CellList)
    for i in range(36):
        print('cell(', CellList2[i].value, ',', CellList2[i].owner, ')')
