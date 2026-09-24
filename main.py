from stats import get_book_words_count
from stats import get_characters_dict
from stats import chars_dict_to_sorted_list

book_frankenstein = "books/frankenstein.txt"

def main(path):
    char_dict = get_characters_dict(get_book_text(path))
    print(f"Found {get_book_words_count(get_book_text(path))} total words")
    char_counts_lists = chars_dict_to_sorted_list(char_dict)
    print(char_counts_lists)

def get_book_text(path_file):
    with open (path_file) as f:
        file_contents = f.read()
        return file_contents

main(book_frankenstein)