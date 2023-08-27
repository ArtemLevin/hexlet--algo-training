from random import randint


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = True


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = [[Cell() for _ in range(self.N)] for _ in range(self.N)]
        self.init()

    def init(self):
        mineDict = {}
        i = 0
        while i < self.M:
            a = randint(0, self.N - 1)
            b = randint(0, self.N - 1)
            if (a, b) not in mineDict.values():
                mineDict[i] = (a, b)
                self.pole[a][b] = Cell(0, True)
                i += 1
        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self.N):
            for y in range(self.N):
                if not self.pole[x][y].mine:
                    mines = sum(
                        (self.pole[x + i][y + j].mine for i, j in indx if 0 <= x + i < self.N and 0 <= y + j < self.N))
                    self.pole[x][y].around_mines = mines

    def show(self):
        for row in self.pole:
            print(*map(lambda x: '#' if not x.fl_open else x.around_mines if not x.mine else '*', row))


pole_game = GamePole(10, 12)
pole_game.show()
