class Player:
    """
    Класс принимает имя и слова пользователя
    """
    def __init__(self, name: str):
        self.name = name
        self.entered_words = []

    def len_entered_words(self):
        """
        :return: количество слов в списке
        """
        return len(self.entered_words)

    def app_entered_words(self, user_answer):
        """
        :param user_answer:  добавляет слова пользователя в список
        """
        self.entered_words.append(user_answer)

    def check_entered_words(self, user_answer):
        """
        :param user_answer: пользователь вводит слово,
        :return: проверяет на схожие ответы
        """
        return user_answer in self.entered_words

    def __repr__(self):
        return f"Player {self.name} {self.entered_words}"
