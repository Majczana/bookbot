def get_book_words_count(book):
    book_lenght = book.split()
    return len(book_lenght)

def get_characters_dict(text):
    char_counts = {}    
    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts


def sort_on(character_counts: tuple[str, int]) -> int:
    return character_counts[1]

def chars_dict_to_sorted_list(char_counts: dict[str, int]):
    list_char_counts = []
    for i in char_counts:
        list_char_counts.append((i, char_counts[i]))
    return sorted(list_char_counts, reverse=True, key=sort_on)


