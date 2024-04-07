def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    #print(f"{num_words} words found in the document")
    each_letter_count = get_num_char(text)
    #print(each_letter_count)
    list_sorted = sorted_letters_list(each_letter_count)
    print(list_sorted)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_char(text):
    letters = {}
    lower_text = text.lower()

    for char in lower_text:
        if ('a' <= char <= 'z'):
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] = letters[char] + 1
    return letters

def sorted_letters_list(letters_dict):
    letters_list = []
    for letter, count in letters_dict.items():
        letters_list.append({'letter' :letter, 'count': count})
    
    letters_list.sort(reverse=True, key = lambda x: x['count'])
    return letters_list



main()