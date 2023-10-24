#!/usr/bin/python3.9


import os
import random


def main():
    letters_in_word = []
    letters_in_word_spots = {}
    letters_in_correct_spot = {}
    letters_in_correct = []
    letters_unavailable = []
    print("")
    print(" Type in your guess.")
    print("")
    first_guess = input("\u001b[35m     > \u001b[0m")
    if len(first_guess) < 5 or len(first_guess) > 5:
        print("     Your guess needs to be 5 letters long.")
        return main()
    check_colors(first_guess, letters_in_word_spots, letters_in_word, letters_in_correct, letters_in_correct_spot, letters_unavailable)
    print("")
    print(" Educated Guess: {0}".format(get_word(letters_in_word, letters_in_word_spots, letters_in_correct, letters_in_correct_spot, letters_unavailable)))
    print("")
    print("")
    print(" Type in your guess.")
    print("")
    first_guess = input("\u001b[35m     > \u001b[0m")
    if len(first_guess) < 5 or len(first_guess) > 5:
        print("     Your guess needs to be 5 letters long.")
        return main()
    check_colors(first_guess, letters_in_word_spots, letters_in_word, letters_in_correct, letters_in_correct_spot, letters_unavailable)
    print("")
    print(" Educated Guess: {0}".format(get_word(letters_in_word, letters_in_word_spots, letters_in_correct, letters_in_correct_spot, letters_unavailable)))
    print("")
    print("")
    print(" Type in your guess.")
    print("")
    first_guess = input("\u001b[35m     > \u001b[0m")
    if len(first_guess) < 5 or len(first_guess) > 5:
        print("     Your guess needs to be 5 letters long.")
        return main()
    check_colors(first_guess, letters_in_word_spots, letters_in_word, letters_in_correct, letters_in_correct_spot, letters_unavailable)
    print("")
    print(" Educated Guess: {0}".format(get_word(letters_in_word, letters_in_word_spots, letters_in_correct, letters_in_correct_spot, letters_unavailable)))
    print("")
    print("")
    print(" Type in your guess.")
    print("")
    first_guess = input("\u001b[35m     > \u001b[0m")
    if len(first_guess) < 5 or len(first_guess) > 5:
        print("     Your guess needs to be 5 letters long.")
        return main()
    check_colors(first_guess, letters_in_word_spots, letters_in_word, letters_in_correct, letters_in_correct_spot, letters_unavailable)
    print("")
    print(" Educated Guess: {0}".format(get_word(letters_in_word, letters_in_word_spots, letters_in_correct, letters_in_correct_spot, letters_unavailable)))
    print("")
    print("")
    print(" Type in your guess.")
    print("")
    first_guess = input("\u001b[35m     > \u001b[0m")
    if len(first_guess) < 5 or len(first_guess) > 5:
        print("     Your guess needs to be 5 letters long.")
        return main()
    check_colors(first_guess, letters_in_word_spots, letters_in_word, letters_in_correct, letters_in_correct_spot, letters_unavailable)
    print("")
    print(" Educated Guess: {0}".format(get_word(letters_in_word, letters_in_word_spots, letters_in_correct, letters_in_correct_spot, letters_unavailable)))
    print("")
    print("")
    print(" Type in your guess.")
    print("")
    first_guess = input("\u001b[35m     > \u001b[0m")
    if len(first_guess) < 5 or len(first_guess) > 5:
        print("     Your guess needs to be 5 letters long.")
        return main()
    check_colors(first_guess, letters_in_word_spots, letters_in_word, letters_in_correct, letters_in_correct_spot, letters_unavailable)
    print("")
    print(" Educated Guess: {0}".format(get_word(letters_in_word, letters_in_word_spots, letters_in_correct, letters_in_correct_spot, letters_unavailable)))
    print("")
    


def get_word(yellow_letters, yellow_letters_in_spots, green_letters, green_letters_json, gray_letters):
    listwords = open("./words.txt", "r")
    listwords = listwords.readlines()
    words = []
    words_to_remove = []
    # Remove \n
    for word in listwords:
        words.append(word.split("\n")[0])

    # Remove all words with unavailable letters
    for word in words:
        for letter in word:
            for unavailable in gray_letters:
                if letter == unavailable:
                    try:
                        words_to_remove.append(word)
                    except ValueError:
                        pass
            if letter in green_letters:
                if not green_letters_json[letter] == word.index(letter):
                    words_to_remove.append(word)
            elif not len(yellow_letters) == 0:
                for yellow in yellow_letters:
                    try:
                        if not yellow in word:
                            words_to_remove.append(word)
                        elif word.index(letter) == yellow_letters_in_spots[letter]:
                            words_to_remove.append(word)
                    except:
                        pass
            if not len(green_letters) == 0:
                for greenl in green_letters:
                    if not word[green_letters_json[greenl]] == greenl:
                        words_to_remove.append(word)


    for target in words_to_remove:
        try:
            words.remove(target)
        except ValueError:
            pass

    return random.choice(words)



    
def check_colors(guess, yellow_letters_in_spots, yellow_letters, green_letters, green_letters_json, gray_letters):
    for letter in guess:
        print("")
        print(" Is {0} in green, yellow, or gray? (G/Y/N)".format(letter))
        print("")
        guess_letter_color = input("\u001b[35m     > \u001b[0m").lower()
        if not guess_letter_color == "g" and not guess_letter_color == "y" and not guess_letter_color == "n":
            print("     The choice needs to be G for Green, Y for Yellow, or N for Gray.")
            return check_colors(guess)
        elif guess_letter_color == "y":
            yellow_letters += letter
            yellow_letters_in_spots[letter] = guess.index(letter)
        elif guess_letter_color == "n":
            gray_letters += letter
        elif guess_letter_color == "g":
            green_letters_json[letter] = guess.index(letter)
            green_letters += letter


if __name__ == "__main__":
    try:
        os.system("clear")
        print("")
        os.system("printf \u001b[35m && figlet \" S O L V E R\" && printf \u001b[0m")
        os.system("printf \u001b[35m\" [ Developed by ZCQ ]\n\"\u001b[0m")
        main()
    except KeyboardInterrupt:
        print("")
        pass
