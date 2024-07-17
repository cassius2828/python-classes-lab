class Game:
    def __init__(
        self,
        turn="x",
        tie=False,
        winner=None,
        board={
            "a1": None,
            "b1": None,
            "c1": None,
            "a2": None,
            "b2": None,
            "c2": None,
            "a3": None,
            "b3": None,
            "c3": None,
        },
    ):
        self.turn = turn
        self.tie = tie
        self.winner = winner
        self.board = board

    # start the game
    def play_game(self):
        print("Welcome to the tic tac toe game of the century")
        self.render()
        self.get_move()

    # display the current state of the board
    def print_board(self):
        b = self.board
        print(
            f"""
        A   B   C
    1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
        ----------
    2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
        ----------
    3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
  """
        )

    # display message of game status to user
    def print_message(self):
        if self.tie:
            print(f"Tie game!")
            return
        elif self.winner:
            print(f"{self.winner} wins the game!")
            return
        else:
            print(f"It's player {self.turn}'s turn")
            self.get_move()

    # displays board and shows message | returns if winner is found
    def render(self):
        self.print_board()
        if self.winner:
            return self.print_message()
        else:
            self.print_message()

    # checks for winner on each turn
    def check_winner(self):
        cols = ["a", "b", "c"]
        rows = [1, 2, 3]

        # diagonal victory
        print(
            f'{self.board["a1"] == self.board["b2"] and self.board["b2"] == self.board["c3"] and self.board["a1"] != None}: diagonal test'
        )
        if (
            self.board["a1"] == self.board["b2"]
            and self.board["b2"] == self.board["c3"]
            and self.board["a1"] != None
        ):
            self.winner = self.turn
            print(self.winner)

            return
        elif (
            self.board["a3"] == self.board["b2"]
            and self.board["b2"] == self.board["c1"]
            and self.board["a3"] != None
        ):
            self.winner = self.turn
            print(self.winner)

            return

        # column victory
        for col in cols:
            # level 1
            col_result = []
            for row in rows:
                #  level 2
                if self.board[f"{col}{row}"] != None:
                    col_result.append(self.board[f"{col}{row}"])

                if len(set(col_result)) == 1 and len(col_result) == 3:
                    self.winner = self.turn
                    print(self.winner)
                    return
        # row victory
        for row in rows:
            # level 1
            row_result = []
            for col in cols:
                #  level 2
                if self.board[f"{col}{row}"] != None:
                    row_result.append(self.board[f"{col}{row}"])

                if len(set(row_result)) == 1 and len(row_result) == 3:
                    self.winner = self.turn
                    print(self.winner)
                    return

    # get move input from player
    def get_move(self):
        # stops game if a winner or tie is found
        if self.winner or self.tie:
            return
        move = input("Select which square you want to play on: ").lower()
        # gracefully handles error if player inputs wrong values
        try:

            # if the move is possible and the place on the board is empty
            if self.board[move] == None and move in self.board:
                # mark the space with whos turn it is
                self.board[move] = self.turn
                # check winner
                self.check_winner()
                # toggle turns
                if self.turn == "x":
                    self.turn = "0"
                else:
                    self.turn = "x"
                    # if there is no winner and all spaces are marked | tie game
                if self.winner is None and all(
                    value is not None for value in self.board.values()
                ):
                    self.tie = True
                # render
            self.render()
            # if a winner is found, return
            if self.winner:
                return
            # error handling
        except:
            print(
                f"Please ensure the space is empty and you type a valid square. Ex: c3"
            )
            # recursive | make player select another space
            return self.get_move()


game_instance = Game()
game_instance.play_game()
