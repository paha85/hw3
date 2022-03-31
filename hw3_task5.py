from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, flag=False):
    """Function chose 3 random words from lists [nouns], [adverbs], [adjectives]"""
    for i in range(n):
        noun = choice(nouns)
        adverb = choice(adverbs)
        adjective = choice(adjectives)
        print(noun, adverb, adjective)


get_jokes(3)

