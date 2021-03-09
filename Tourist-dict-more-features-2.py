"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: tuni.fi:50745580
Name:Oussama Bahri
Email:oussama.bahri@tuni.fi
Solution task 7.6: A tourist dictionary more Features 2
"""

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    spanish_english = {"hola": "hey", "gracias": "thanks", "casa": "home"}
    print("Dictionary contents:")
    separator = ', '
    dict = separator.join(sorted(english_spanish))
    print(dict)


    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish[word]}")
            else:
                print("The word", word, "could not be found from the dictionar"
                                        "y.")


        elif command == "A":
            english_word = input("Give the word to be added in English: ")
            spanish_word = input("Give the word to be added in Spanish: ")
            added_words_english = {english_word:spanish_word}
            english_spanish.update(added_words_english)
            added_words_spanish = {spanish_word:english_word}
            spanish_english.update(added_words_spanish)
            print("Dictionary contents:")
            separator = ', '
            dict = separator.join(sorted(english_spanish))
            print(dict)

        elif command == "R":
            word = input("Give the word to be removed: ")
            if word in english_spanish:
                del english_spanish[word]
            else:
                print(f"The word {word} could not be found from the dictionary."
                      )
        elif command == "P":
            print(" ")
            print("English-Spanish")
            for words in sorted(english_spanish):
                print(f"{words} {english_spanish[words]}")
            print(" ")
            print("Spanish-English")
            for words in sorted(spanish_english):
                print(f"{words} {spanish_english[words]}")
            print(" ")


        elif command == "T":
            text = input("Enter the text to be translated into Spanish: ")
            list = text.split()
            print("The text, translated by the dictionary:")

            for word in list:
                if word in english_spanish:
                    print(f"{english_spanish[word]}", end=' ')
                else:
                    print(word, end=' ')
            print(' ')

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
