from grid.coord import Coord

NUMBER_OF_ROWS = 4
NUMBER_OF_COLUMNS = 4


class Grid(object):

    __grid: list[list[str]]

    __iter_current: Coord

    def __init__(self, grid):
        self.__iter_current = Coord(0, 0)
        self.__grid = grid

    def validate_and_normalize(self):
        if len(self.__grid) != NUMBER_OF_ROWS:
            raise "Invalid number of rows in the provided grid. It should be " + str(NUMBER_OF_ROWS)
        for row in self.__grid:
            if len(row) != NUMBER_OF_COLUMNS:
                raise "Invalid grid provided. At least one of the row don't have the required number of letters " \
                      "(expected : " + str(NUMBER_OF_COLUMNS) + ")"
        for coord in self:
            letter = self.get(coord)
            self.__grid[coord.get_row()][coord.get_column()] = normalize_letter(letter)
            letter = self.get(coord)
            if len(letter) != 1:
                raise "One of the letter in the grid contains more than a single letter."

    def get(self, coord: Coord) -> str:
        if coord.get_row() >= NUMBER_OF_ROWS:
            raise "Invalid row number. Must be < " + str(NUMBER_OF_ROWS)
        if coord.get_column() >= NUMBER_OF_COLUMNS:
            raise "Invalid column number. Must be < " + str(NUMBER_OF_COLUMNS)
        return self.__grid[coord.get_row()][coord.get_column()]

    def __iter__(self):
        self.__iter_current = Coord(0, 0)
        return self

    def __next__(self):
        current_coord = self.__iter_current
        if current_coord.get_column() > NUMBER_OF_COLUMNS - 1 or current_coord.get_row() > NUMBER_OF_ROWS - 1:
            raise StopIteration
        if current_coord.get_column() < NUMBER_OF_COLUMNS - 1:
            self.__iter_current = Coord(current_coord.get_row(), current_coord.get_column() + 1)
            return current_coord
        self.__iter_current = Coord(current_coord.get_row() + 1, 0)
        return current_coord

    def __str__(self) -> str:
        result = ""
        for row in range(NUMBER_OF_ROWS):
            for column in range(NUMBER_OF_COLUMNS):
                result += self.__grid[row][column] + " "
            result += "\n"
        return result


def find_neighbours(coord: Coord) -> list[Coord]:
    result = []
    if coord.get_row() > 0:
        result.append(Coord(coord.get_row() - 1, coord.get_column()))
    if coord.get_row() < NUMBER_OF_ROWS - 1:
        result.append(Coord(coord.get_row() + 1, coord.get_column()))
    if coord.get_column() > 0:
        result.append(Coord(coord.get_row(), coord.get_column() - 1))
    if coord.get_column() < NUMBER_OF_COLUMNS - 1:
        result.append(Coord(coord.get_row(), coord.get_column() + 1))
    return result


def normalize_letter(letter: str):
    return letter.upper().strip()
