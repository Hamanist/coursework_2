class BasicWord:
    """
    Класс получает слова и верные под слова
    """

    def __init__(self, word, valid_word):
        self.word = word
        self.valid_word = valid_word

    def validate_word(self, user_word):
        """
        :param user_word: принимает слово пользователя
        :return: проверят есть ли слово пользователя в списке под слов
        """
        return user_word in self.valid_word

    def number_of_subwords(self):
        """

        :return: количество под слов
        """
        return len(self.valid_word)

    def __repr__(self):
        return f"BasicWord {self.word}  {self.valid_word}"
