

class Coord(object):

    __row: int

    __column: int

    def __init__(self, row: int, column: int):
        self.__row = row
        self.__column = column

    def get_row(self):
        return self.__row

    def get_column(self):
        return self.__column

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__row == other.__row and self.__column == other.__column
        else:
            return False

    def __str__(self) -> str:
        return "[" + str(self.get_row()) + "; " + str(self.get_column()) + "]"
