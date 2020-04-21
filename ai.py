class AI:

    DEPTH = 3

    @staticmethod
    def score(game):
        if game.win():
            return 50 if game.human_turn else -1
        else:
            return 0

    @staticmethod
    def recurse(game, depth):

        # break conditions
        # you won the game
        # depth == 0 reached limit
        if game.win() or depth == 0:
            return AI.score(game)
        else:
            newstates = []
            # set of actions
            for col in [0, 1, 2, 3]:
                # ignore invalid moves
                if not game.valid_move(col): continue

                # create new state
                newstate = game.__deepcopy__(None)
                newstate.col_check(col)
                newstates.append((newstate, col))


            # return sum of children states
            return sum(
                # recursively calculate the score of new states
                [
                    AI.recurse(newstate, depth - 1)
                    for (newstate, col) in newstates
                ]
            )


    @staticmethod
    def move(game):

        # set of actions
        newstates = []
        for col in [0, 1, 2, 3]:
            # ignore invalid moves
            if not game.valid_move(col): continue

            # create new state
            newstate = game.__deepcopy__(None)
            newstate.col_check(col)
            newstates.append((newstate, col))


        # choose state with maximum score
        return max(
            # recursively calculate the score of new states
            [
                (AI.recurse(newstate, AI.DEPTH), col)
                for (newstate, col) in newstates
            ]
        )[1]
