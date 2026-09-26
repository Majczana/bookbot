import sys
from stats import get_book_words_count
from stats import get_characters_dict
from stats import chars_dict_to_sorted_list


def main(path):

    char_dict = get_characters_dict(get_book_text(path))
    print('============ BOOKBOT ============')
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_book_words_count(get_book_text(path))} total words")
    print("--------- Character Count -------")
    char_counts_lists = chars_dict_to_sorted_list(char_dict)
    for char in char_counts_lists:
        if char[0].isalpha():
            print(f"{char[0]}: {char[1]}")
    print("============= END ===============")

def get_book_text(path_file):
    with open (path_file) as f:
        file_contents = f.read()
        return file_contents
    
if len(sys.argv) >= 2:
    book_path_name = sys.argv[1]
    main(book_path_name)
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)