def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    def sum_words(text):
        words = text.split()
        return len(words)

    word_count = sum_words(file_contents)
    print(f"The book contains {word_count} words.")

main()