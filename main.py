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
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        return f"File not found: {file_path}"

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
    words = text.split()
    return len(words)

def main():
    book_string = get_book_text("books/frankenstein.txt")
    word_count = count_words_in_text(book_string)
    print(f"{word_count} words found in the document")
    pass

main()