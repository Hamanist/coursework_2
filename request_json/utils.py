import json
import random
import requests
import urllib3

from classes_for_the_game.basic_word import BasicWord

urllib3.disable_warnings()

LINK = 'https://jsonkeeper.com/b/MZO8'


def load_random_word(link):
    response = requests.get(LINK, verify=False)
    file_json = json.loads(response.text)
    random.shuffle(file_json)
    questions = []
    for data in file_json:
        word = data['word']
        answer = data['subwords']
        basic_word = BasicWord(word, answer)
        questions.append(basic_word)
    return questions


print(load_random_word(LINK))
