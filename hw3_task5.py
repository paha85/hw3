from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, flag=False):
    """Function chose 3 random words from lists [nouns], [adverbs], [adjectives]"""
    for i in range(n):
        word_1 = choice(nouns)
        word_2 = choice(adverbs)
        word_3 = choice(adjectives)
        joke = f'{word_1} {word_2} {word_3}'
        print(joke)
        duplex = []
        if flag:
            duplex = joke.split()
            for noun in nouns:
                for punch in duplex:
                    if noun == punch:
                        nouns.remove(noun)
            for adverb in adverbs:
                for punch in duplex:
                    if adverb == punch:
                        adverbs.remove(adverb)
            for adjective in adjectives:
                for punch in duplex:
                    if adjective == punch:
                        adjectives.remove(adjective)


get_jokes(n=3, flag=True)
