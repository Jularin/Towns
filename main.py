import sys
from datetime import datetime
import time

towns = []
words_from_player_count = 0
words_from_computer_count = 0

with open('Towns.txt', encoding='utf-8') as f:
    for line in f:
        towns.append(line[:len(line) - 1])


def exit_from_game():
    with open("logs.txt", 'a', encoding='utf-8') as logs:
        logs.write("{} Game ended \n".format((datetime.now().strftime("%d-%m-%Y %H:%M"))))
    time.sleep(1000)
    sys.exit("Спасибо за игру!\nПока")


def find_last_letter(word):
    if word[-1] == 'ь' or word[-1] == 'ъ': #if word[-1] == 'ь' or word[-1] == 'ъ' or word[-1] == 'ы'
        last_letter = word[-2]
    else:
        last_letter = word[-1]
    return last_letter


def start():
    global towns
    """Function for first word. Return last letter for next word"""
    first_town = input("Привет! Чтобы выйти из игры напиши Выход \nВведите название города: ")
    if first_town.lower() == 'выход':
        exit_from_game()
    with open("logs.txt", 'a', encoding='utf-8') as logs:
        logs.write("{} First word - {} \n".format((datetime.now().strftime("%d-%m-%Y %H:%M")), first_town))
    if first_town in towns:
        print("Неплохо! Такой город существует!")
        towns.remove(first_town)
    else:
        print("Такого города не существует( \nПопробуй ещё раз")
        return start()

    return find_last_letter(first_town)


def find_next_word(last_letter):
    global towns
    for word in towns:
        if word[0].lower() == last_letter:
            print("Следующее слово: " + word + "\nТы должен написать слово на букву: " + find_last_letter(word).upper())
            towns.remove(word)
            with open("logs.txt", 'a', encoding='utf-8') as logs:
                logs.write("{} Next town from computer - {} \n".format((datetime.now().strftime("%d-%m-%Y %H:%M")), word))
            return word
    with open("logs.txt", 'a', encoding='utf-8') as logs:
        logs.write("{} Computer can't find word with letter '{}' \n".format((datetime.now().strftime("%d-%m-%Y %H:%M")),
                                                                         last_letter))
    return None


def parse_word(last_letter):
    town = input("Введите название города: ")
    if town.lower() == 'выход':
        exit()
    with open("logs.txt", 'a', encoding='utf-8') as logs:
        logs.write("{} Next word from player - {} \n".format((datetime.now().strftime("%d-%m-%Y %H:%M")), town))
    if town in towns and last_letter == town[0].lower():
        print("Неплохо! Такой город существует!")
        towns.remove(town)
    elif town in towns and last_letter != town[0].lower():
        print("Город сущетсвует, но первая буква не является последней буквой предыдущего слова, попробуйте ещё раз")
        return parse_word(last_letter)
    else:
        print("Такого города не существует( \nПопробуй ещё раз")
        return parse_word(last_letter)

    return find_last_letter(town)


def game():
    global towns
    with open("logs.txt", 'a', encoding='utf-8') as logs:
        logs.write("{} Game started \n".format((datetime.now().strftime("%d-%m-%Y %H:%M"))))
    last_letter = start()
    next_word = find_next_word(last_letter)
    while 1:
        if next_word is None:

            sys.exit("Спасибо за игру! Я не могу найти слово")

        last_letter = parse_word(find_last_letter(next_word))
        next_word = find_next_word(last_letter)


game()
