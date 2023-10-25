from request_json.utils import load_random_word
from classes_for_the_game.players import Player


def main():
    word = load_random_word()
    print('Введите имя игрока')
    user_name = input("-->  ").title()
    player = Player(user_name)
    print(f'Привет, {player.name}!')
    print(f'Составьте {word.number_of_subwords()} слов из слова {word.word}')
    print('Слова должны быть не короче 3 букв')
    print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
    print('Поехали, ваше первое слово?')

    while player.len_entered_words() != word.number_of_subwords():
        user_answer = input("Введите слово:  ").lower()
        if user_answer == "stop" or user_answer == "стоп":
            break
        elif len(user_answer) <= 2:
            print("Cлишком короткое слово")
            continue
        elif player.check_entered_words(user_answer):
            print("Уже использовано")

        elif word.validate_word(user_answer):
            player.app_entered_words(user_answer)
            print('Верно')
        else:
            print('Не верно')

    print(f"Игра завершена, вы угадали {player.len_entered_words()} слов!")


if __name__ == '__main__':
    main()
