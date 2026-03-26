# Accepts the text from book as string and returns number of words in string
def count_words(book_text):
    words = book_text.split()
    return len(words)

# Takes text from book as string and returns the number of times each char appears in string
def count_characters_dict(book_text):
    char_dict = {}
    for c in book_text:
        lowered = c.lower()
        char_dict[lowered] = char_dict.get(lowered, 0) + 1
    return char_dict

# Helper function to return "num" key of each dict
def get_num(item):
    return item["num"]

# Takes dict of chars and their counts and returns a sorted list of dicts
def sorted_dicts(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        sorted_list.append({"char": char, "num": count})
    sorted_list.sort(key=get_num, reverse=True)
    return sorted_list