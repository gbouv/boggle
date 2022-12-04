LEAF_CHAR = "_"


def load_dictionary(file_path: str) -> dict[str, dict]:
    dictionary = {}
    file = open(file_path, 'r')
    for word in file.readlines():
        normalized_word = normalize_word(word)
        populate_dictionary(normalized_word, dictionary)
    return dictionary


def populate_dictionary(word: str, dictionary: dict[str, dict]):
    if len(word) == 0:
        dictionary[LEAF_CHAR] = {}
        return
    first_letter = word[0]
    if first_letter not in dictionary:
        dictionary[first_letter] = {}
    populate_dictionary(word[1:], dictionary[first_letter])


def normalize_word(word: str) -> str:
    return word.upper().strip()
