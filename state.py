import copy

from board import Board
from ai import AI

class ColumnFullException(Exception):
    pass

class WrongTurnException(Exception):
    pass

class State:

    HUMAN = 1
    COMPUTER = 4

    def __init__(self):
        self.human_turn = True
        self.turn_count = 0
        self.board = Board.new()
        self.last_turn = (-1, -1)

    def __repr__(self):
        return 'State()'

    def __str__(self):
        return '\n'.join([f'Player turn: {self.human_turn}', f'Turn count: {self.turn_count}', self.board.__str__()])

    def __deepcopy__(self, memo):
        temp = State()
        temp.human_turn = self.human_turn
        temp.turn_count = self.turn_count
        temp.last_turn = self.last_turn
        temp.board = self.board.__deepcopy__(None)
        return temp

    @staticmethod
    def new():
        return State()

    def valid_move(self, col):
        choice = self.choices(col)
        return len(choice) != 0

    def choices(self, col):
        return [row for row in [0, 1, 2, 3] if self.board.check(row, col) == 0]

    def col_check(self, col):
        choice = self.choices(col)
        if (len(choice) == 0):
            raise ColumnFullException
        else:
            row = choice[0]
            val = State.HUMAN if self.human_turn else State.COMPUTER
            self.board.select(row, col, val)
            self.turn_count += 1 
            self.last_turn = (row, col)
            self.human_turn = not self.human_turn

    def human_choice(self, col):
        if self.human_turn:
            try:
                self.col_check(col)
                if self.win():
                    print('Game over human won')
            except ColumnFullException as e:
                raise e
        else:
            raise WrongTurnException()

    def ai_choice(self):
        if not self.human_turn:
            self.col_check(AI.move(self))
            if self.win():
                print('Game over computer won')
        else:
            raise WrongTurnException()

    def win(self):
        line_offsets = [
            # vertical
            [(0, 0), (1, 0), (2, 0)],
            [(-1, 0), (0, 0), (1, 0)],
            [(-2, 0), (-1, 0), (0, 0)],

            # horizontal
            [(0, 0), (0, 1), (0, 2)],
            [(0, -1), (0, 0), (0, 1)],
            [(0, -2), (0, -1), (0, 0)],
            
            # diagonal
            [(0, 0), (1, 1), (2, 2)],
            [(-2, -2), (-1, -1), (0, 0)]

            # add more states as required
        ]

        # helper function to add elements of two tuples
        def add(tp1, tp2): return (tp1[0] + tp2[0], tp1[1] + tp2[1])

        return any (
            [
                # evaluate sum of values calculated from a line
                sum(values) in [3, 12]
                for values in [
                    [
                        # find position values by adding offset with last turn position
                        self.board.check(*add(self.last_turn, offset))
                        # iterate each offset in a single line offset
                        for offset in line_offset
                        # only add keep position if it is within board boundaries
                        if self.board.safe(*add(self.last_turn, offset))
                    ]

                    # iterate each line offset
                    for line_offset in line_offsets
                ]
            ]
        )

if __name__ == "__main__":
    s = State.new()
    s.human_choice(1)
    s.ai_choice()
    assert(s.win() == False)
    s.human_choice(1)
    s.ai_choice()
    assert(s.win() == False)
