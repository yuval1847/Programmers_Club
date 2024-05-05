def commonWords(text, n):
    # The function gets a string and an integer.
    # The function returns a list in length of the given integer of the most common words in the text
    words = text.lower().split()
    word_count = {}
    for word in words:
        normalized_word = word.strip(".,!?;:'\"()[]{}")
        if normalized_word:
            if normalized_word in word_count:
                word_count[normalized_word] += 1
            else:
                word_count[normalized_word] = 1
    sorted_words = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))
    top_words = [word for word, _ in sorted_words[:n]]
    return top_words

if __name__ == "__main__":
    fileContent = ""
    n = 0
    try:
        with open(input("Enter a file name: "), "r") as file:
            fileContent = file.read()
        n = int(input("Enter the amount of common words: "))
    except TypeError:
        print("⚠ Error: The file name should be a string or the amount of common words should be integer!")
    except FileNotFoundError:
        print("⚠ Error: This file doesn't exist!")
    
    print(f"The most common words: {', '.join(commonWords(fileContent, n))}")