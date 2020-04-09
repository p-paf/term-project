from board import Board

class ColumnFullException(Exception):
    pass

class State:

    def __init__(self):
        self.human_turn = True
        self.turn_count = 0
        self.board = Board.new()
        self.last_turn = (-1, -1)

    def __repr__(self):
        return 'State(0)'

    def __str__(self):
        return '\n'.join([f'Player turn: {self.human_turn}', f'Turn count: {self.turn_count}', self.board.__str__()])

    def col_check(self, col, val):
        choice = [row for row in [0, 1, 2, 3] if self.board.check(row, col) == 0]
        if (len(choice) == 0):
            raise ColumnFullException
        else:
            row = choice[0]
            self.board.select(row, col, val)
            self.turn_count += 1 
            self.last_turn = (row, col)

    def human_choice(self, col):
        self.col_check(col, 1)
        self.human_turn = False

    def ai_choice(self, col):
        self.col_check(col, 2)
        self.human_turn = True

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
        ]

        # helper function to add elements of two tuples
        def add(tp1, tp2): return (tp1[0] + tp2[0], tp1[1] + tp2[1])

        return any (
            [
                # evaluate sum of values calculated from a line
                sum(values) in [3, 6]
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
