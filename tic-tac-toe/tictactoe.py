from typing import List


class TicTacToe:
    def __init__(self) -> None:
        self.cells: List[List[str]] = [list(' ' * 3) for i in range(3)]
        self.current_player: str = 'X'
        self.round: int = 1

    def start(self) -> None:
        """ Starts the game """

        while True:
            self.__print_cells()
            self.__fill_cell(self.__get_coord())

            self.round += 1

            """
            Check the win from round 5 because its the minimal possible state.

            The check winner function is only called on this condition because
            of short-circuit evaluation.
            """
            if (self.round >= 5) and (self.__is_game_finished() is True):
                break

            self.__switch_player()

    def __print_cells(self) -> None:
        """ Print the cells from cells matrix """

        print('-' * 9)

        for line in self.cells:
            print(f'| {line[0]} {line[1]} {line[2]} |')

        print('-' * 9)

    def __get_coord(self) -> List[int]:
        """ Get cell coordinates (column, row) from user and validates it """

        coordinates: List[int] = []

        while True:
            user_input: str = input('Enter the coordinates:')

            try:
                coordinates = [int(num) for num in user_input.split()]

                if any(n not in range(1, 4) for n in coordinates):
                    print('Coordinates should be from 1 to 3!')
                else:
                    break
            except ValueError:
                print('You should enter numbers!')

        return coordinates

    def __fill_cell(self, coordinates: List[int]) -> None:
        """ Fill the cell according to the coordinates position """

        """
        The coordinates are given (column, row), following this layout:
        (1, 3) (2, 3) (3, 3)
        (1, 2) (2, 2) (3, 2)
        (1, 1) (2, 1) (3, 1)

        To make things easier, the coordinates are changed to (row, column):
        (3, 1) (3, 2) (3, 3)
        (2, 1) (2, 2) (2, 3)
        (1, 1) (1, 2) (1, 3)
        """
        coordinates.reverse()

        """
        Now we have the following situation, we need to convert the coordinates
        position to the cells position:

        Coordinates positions       Cells positions
        (3, 1) (3, 2) (3, 3)        [0, 0] [0, 1] [0, 2]
        (2, 1) (2, 2) (2, 3)        [1, 0] [1, 1] [1, 2]
        (1, 1) (1, 2) (1, 3)        [2, 0] [2, 1] [2, 2]
        """
        row = abs(coordinates[0] - 3)
        column = coordinates[1] - 1

        # Fill the cell with player
        if self.cells[row][column] == ' ':
            self.cells[row][column] = self.current_player
        else:
            print('This cell is occupied! Choose another one!')
            self.__fill_cell(self.__get_coord())

    def __switch_player(self) -> None:
        self.current_player = 'X' if self.current_player == 'O' else 'O'

    def __is_game_finished(self) -> bool:
        """ Check the state of cells and prints the winner. Possible states:

        - Draw: when no side has a 3 in a row and the field has no empty cells
        - X wins: when the field has 3 X in a row
        - O wins: when the field has 3 O in a row
        """

        winner: str = self.__check_cells()

        finish: bool = False
        msg: str = ''

        # No winners and last round
        if (winner is '') and (self.round is 9):
            msg = 'Draw'
            finish = True
        elif (winner is 'X') or (winner is 'O'):
            msg = 'O wins' if winner is 'O' else 'X wins'
            finish = True

        if finish:
            self.__print_cells()
            print(msg)

        return finish

    def __check_cells(self) -> str:
        """ Loop trough the cells matrix and find the winner(s) """

        # Create cells variable to make comparsions more legible
        cells: List[List[str]] = self.cells

        # Helper inner function to compare our cells and add to list
        def is_equals(cell_1: str, cell_2: str, cell_3: str) -> bool:
            if (cell_1 is cell_2 is cell_3) and (cell_1 is not ' '):
                return True
            return False

        # Check rows
        for row in range(len(cells)):
            if is_equals(cells[row][0], cells[row][1], cells[row][2]):
                return cells[row][0]

        # Check columns
        for column in range(len(cells)):
            if is_equals(cells[0][column], cells[1][column], cells[2][column]):
                return cells[0][column]

        # Check primary diagonal \
        if is_equals(cells[0][0], cells[1][1], cells[2][2]):
            return cells[0][0]

        # Check secondary diagonal /
        if is_equals(cells[2][0], cells[1][1], cells[0][2]):
            return cells[2][0]

        return ''


if __name__ == '__main__':
    TicTacToe().start()
