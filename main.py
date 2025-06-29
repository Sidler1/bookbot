from stats import count_words_in_text, count_characters_in_text, sort_characters_by_frequency
import sys


def get_book_text(file_path: str) -> str:
    """
    Read and return the contents of a text file.

    This function attempts to open and read a file specified by the given file path.
    If successful, it returns the entire contents of the file as a string.
    If the file is not found, it returns an error message.

    Args:
        file_path (str): The path to the text file to be read.

    Returns:
        str: The contents of the file as a string if successful,
             or an error message if the file is not found.
    """
    print(f"Analyzing book found at {file_path}...")
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        return f"File not found: {file_path}"


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    book_string = get_book_text(sys.argv[1])
    count_words_in_text(book_string)
    character_count = count_characters_in_text(book_string)
    sort_characters_by_frequency(character_count)
    print("============= END ===============")
    pass


main()
