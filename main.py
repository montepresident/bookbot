def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    def sum_words(text):
        return len(text.split())

    word_count = sum_words(file_contents)
    print(f"The book contains {word_count} words.")

    def frequency(text):
        dictionary = {}
        for words in text.lower():
            for char in words:
                if char == words:
                    dictionary[text] += 1
        return dictionary
    characters = frequency(file_contents)
    print(f"Here are the details about the characters: {characters}")
    
main()