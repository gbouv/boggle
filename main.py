import json

from dictionary import builder
from finder import find_all_words
from grid.grid import Grid

if __name__ == '__main__':
    grid = Grid([
        ["S", "T", "c", "i"],
        ["e", "R", "r", "E"],
        ["o", "t", "e", "b"],
        ["o", "t", "i", "e"],
    ])
    print("Solving grid:\n{0}".format(grid))

    grid.validate_and_normalize()

    dictionary = builder.load_dictionary('resources/dictionary.txt')

    all_words = find_all_words(dictionary, grid)
    total_points = 0
    for word in all_words:
        total_points += word.compute_points()
        print(word.print(grid))
    print("Number of words found: {0}".format(len(all_words)))
    print("Maximum number of points: {0}".format(total_points))
