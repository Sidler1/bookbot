def count_words_in_text(text: str) -> int:
    """
    Count the number of words in a given text.

    This function takes a string of text as input, splits it into words,
    and returns the total number of words found.

    Args:
        text (str): The input text to be analyzed.

    Returns:
        int: The number of words in the input text.
    """
    print("----------- Word Count ----------")
    words = text.split()
    word_count = len(words)
    print(f"Found {word_count} total words")
    return word_count


def count_characters_in_text(text: str) -> dict[str, int]:
    """
    Count the occurrences of each character in a given text.

    This function takes a string of text as input, converts it to lowercase,
    and counts the occurrences of each character. It returns a dictionary
    where each key is a character and the corresponding value is the number
    of times that character appears in the text.

    Args:
        text (str): The input text to be analyzed. This can be a single word,
                    a sentence, or a longer piece of text.

    Returns:
        dict[str, int]: A dictionary where each key is a character (str) and
                        each value is the count of that character's occurrences (int)
                        in the input text. The dictionary includes all characters
                        present in the text, including spaces and punctuation.

    Example:
        >>> count_characters_in_text("Hello, World!")
        {'h': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}
    """
    word_list = text.lower()
    character_counts = {}
    for char in word_list:
        character_counts[char] = character_counts.get(char, 0) + 1
    return character_counts


def sort_characters_by_frequency(character_counts: dict[str, int]) -> dict[str, int]:
    """
    Sort characters by their frequency in descending order.

    This function takes a dictionary of character counts and returns a new dictionary
    with the same key-value pairs, but sorted by the count values in descending order.
    It also prints a header for the character count section.

    Args:
        character_counts (dict[str, int]): A dictionary where keys are characters (str)
                                           and values are their respective counts (int).

    Returns:
        dict[str, int]: A new dictionary with the same key-value pairs as the input,
                        but sorted by count values in descending order.

    Example:
        >>> sort_characters_by_frequency({'a': 3, 'b': 1, 'c': 2})
        {'a': 3, 'c': 2, 'b': 1}
    """
    print("--------- Character Count -------")
    sorted_characters = dict(sorted(character_counts.items(), key=lambda x: x[1], reverse=True))
    for char, count in sorted_characters.items():
        if char.isalpha():  # only print alphabetic characters
            print(f"{char}: {count}")
    return sorted_characters
