def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    def sum_words(start, stop):
        book_string = []    
        for words in file_contents(start, stop):
            book_string.append(words)
        return book_string.index()

main()