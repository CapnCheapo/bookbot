import sys
from stats import count_words, count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    contents = get_book_text(sys.argv[1])
    print("----------- Word Count ----------")
    num_words = count_words(contents)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    count = count_characters(contents)
    for letter in count:
        print(f"{letter}: {count[letter]}")
    print("============= END ===============")

main()
