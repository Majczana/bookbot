def main(path):
    print(f"Found {get_book_words_count(path)} total words")

def get_book_text(path_file):
    with open (path_file) as f:
        file_contents = f.read()
        return file_contents

def get_book_words_count(book):
    book_text = get_book_text(book)
    book_lenght = book_text.split()
    return len(book_lenght)

main("books/frankenstein.txt")