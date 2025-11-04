from stats import get_num_words
from stats import get_book_text


def main():
    book_name = "frankenstein.txt"
    book_text = get_book_text(book_name)
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")
    print(book_text)

main()