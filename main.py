#bookbot

def get_book_text():
    with open("./books/frankenstein.txt") as f:
        return f.read()

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    frankenstein = file_contents
    book_list = frankenstein.split()
    word_count = 0
    for i in book_list:
        word_count += 1
    
    print(f"{word_count} words found in this document!")
   

def count_letters():
    book_text = get_book_text()  
    uncaps = book_text.lower()
    frank_dict = {}
    for i in uncaps:
        if i.isalpha():
            if i in frank_dict:
                frank_dict[i] += 1
            else:
                frank_dict[i] = 1
    return frank_dict
       

def letter_count_list():
    counted_list = count_letters()
    
    for i in counted_list:
        print(f"The '{i}' character was found {counted_list[i]} times")

'''
This was their solution:
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
'''

    

print("--- Begin report of books/frankenstein.txt ---")
main()
letter_count_list()
print("--- End report ---")