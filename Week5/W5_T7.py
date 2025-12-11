DELIMITER = ","
def collectWords():
    Word = []
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        Word.append(word)
    return DELIMITER.join(Word)


def analyseWords(Word_string):
    word_list = Word_string.split(DELIMITER)
    if not Word_string:
        print("- 0 Words")
        print("- 0 Characters")
        print("- 0.00 Average word length")
        return

    word_count = len(word_list)
    char_count = sum(len(word) for word in word_list)
    avg_length = char_count / word_count

    print(f"- {word_count} Words")
    print(f"- {char_count} Characters")
    print("- {:.2f} Average word length".format(avg_length))

def main():
    print("Program starting.")
    Word = collectWords()
    analyseWords(Word)
    print("Program ending.")


if __name__ == "__main__":
    main()
