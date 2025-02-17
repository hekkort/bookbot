def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()       
        #print(file_contents)
        #print(count_words(file_contents))
        #print(count_chars(file_contents))
        print(report(file_contents))

def count_words(book):
    word_count = len(book.split())
    return word_count

def count_chars(book):
    counts = {}
    lower_book = book.lower()
    for char in lower_book:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def report(book):
    dict = count_chars(book)
    string = "--- Begin report of books/frankenstein.txt ---\n"
    string = string + str(count_words(book)) + " words found in the document\n\n"
    for k, v in dict.items():
        if k.isalpha():
            string = string + f"The '{k}' character was found '{v}' times\n"
    return string + "--- End report ---"
    


main()