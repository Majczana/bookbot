def get_book_text(book):
    with open(f"books/{book}") as f:
        return f.read()

def get_num_words(text):
    return len(text.split())