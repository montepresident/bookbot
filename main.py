def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    def sum_words(text):
        return len(text.split())

    word_count = sum_words(file_contents)
    print(f"The book contains {word_count} words.")

    def frequency(text):
        dictionary = {}
        for char in text.lower():
            if char.isspace():
                continue
            if char in dictionary:
                dictionary[char] += 1
            else:
                dictionary[char] = 1
                
        return dictionary
    
    characters = frequency(file_contents)
    sorted_dict = dict(sorted(characters.items()))
    
    for keys in sorted_dict:
        print(f"The '{keys}' character was found {sorted_dict[keys]} times.")

main()