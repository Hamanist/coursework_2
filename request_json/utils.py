import json
import random
import requests
import urllib3
from classes_for_the_game.basic_word import BasicWord

urllib3.disable_warnings()

LINK = 'https://jsonkeeper.com/b/MZO8'


def load_random_word():
    """
    Принимает с внешнего ресурса файл json
    :return: экземпляр класса BasicWord перемешивая слова
    """
    response = requests.get(LINK, verify=False)
    file_json = json.loads(response.text)
    random.shuffle(file_json)
    basic_word = BasicWord(file_json[0]["word"], file_json[0]["subwords"])
    return basic_word
