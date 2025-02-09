def main():
    print("--- Begin report of books/frankenstein.txt ---")
    word_count()
    character_count()
    print("--- End report ---")


def word_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    print(f"{len(words)} words found in the document\n")

def character_count():
    characters = {}
    character_list = []
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    for each in file_contents:
        if each.isalpha():
            if each.lower() in characters:
                characters[each.lower()] += 1
            else:
                characters[each.lower()] = 1
    for char, count in characters.items():
        temp = {}
        temp["character"] = char
        temp["num"] = count
        character_list.append(temp)
    character_list.sort(reverse=True, key=sort_on)
    for each in character_list:
        print(f"The '{each["character"]}' character was found {each["num"]} times")
    
def sort_on(dict):
    return dict["num"]

if __name__ == "__main__":
    main()