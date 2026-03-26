import sys
from stats import count_words, count_characters_dict, sorted_dicts

def main():
    # Check if sys.argv has two entries
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1] # path to book file
    text = get_book_text(path)
    num_words = count_words(text)
    character_counts = count_characters_dict(text)
    sort = sorted_dicts(character_counts)

    # Print report
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + path + "...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sort:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")

# Takes a filepath as input and returns the contents of the file (book) as a string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
main()