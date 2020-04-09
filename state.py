from board import Board

class ColumnFullException(Exception):
    pass

class State:

    def __init__(self):
        self.player_turn = True
        self.turn_count = 0
        self.board = Board.new()
        self.last_turn = (-1, -1)

    def __str__(self):
        return '\n'.join([f'Player turn: {self.player_turn}', f'Turn count: {self.turn_count}', self.board.__str__()])

    def col_check(self, col):
        choice = [row for row in [0, 1, 2, 3] if self.board.check(row, col) == 0]
        if (len(choice) == 0):
            raise ColumnFullException
        else:
            return choice[0]

    def player_choice(self, col):
        row = self.col_check(col)
        self.board.select(row, col, 1)
        self.last_turn = (row, col)

    def ai_choice(self, col):
        row = self.col_check(col)
        self.board.select(row, col, 2)
        self.last_turn = (row, col)

    def win(self):
        orientations = [
            # vertical
            [(0, 0), (1, 0), (2, 0)],
            [(-1, 0), (0, 0), (1, 0)],
            [(-2, 0), (-1, 0), (0, 0)],

            # horizontal
            [(0, 0), (0, 1), (0, 2)],
            [(0, -1), (0, 0), (0, 1)],
            [(0, -2), (0, -1), (0, 0)],
        ]

        return any()
