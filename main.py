from dictionary import builder
from finder import find_all_words
from grid.grid import Grid

if __name__ == '__main__':
    grid = Grid([
        ["S", "E", "T", "I"],
        ["S", "R", "E", "E"],
        ["Z", "P", "L", "S"],
        ["V", "U", "J", "S"],
    ])

    print("Solving grid:")
    print(str(grid))

    grid.validate_and_normalize()

    dictionary = builder.load_dictionary('resources/dictionary.txt')

    all_words = find_all_words(dictionary, grid)
    total_points = 0
    for word in all_words:
        total_points += word.compute_points()
        print(word.print(grid))

    print("Maximum number of points: " + str(total_points))
