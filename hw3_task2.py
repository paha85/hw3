words = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
    'thirteen': 'чертова дюжина'
}

words_cap = {k.capitalize(): v.capitalize() for k, v in words.items()}


def num_translate_adv(i):
    """Func returns value from dict {words} or {words_cap} for capitalized words"""
    if i == i.capitalize():
        return words_cap.get(i)
    elif i != i.capitalize():
        return words.get(i)


word = (input('Hello, welcome to the translator from English to Russian!\n'
              'Pls enter number from one to ten or quite to exit: '))
while True:
    if word == 'quite':
        print('Thanks and goodbye!')
        break
    elif word not in words.keys() and word not in words_cap.keys():
        print(f'I\'m sry, I don\'t know word {word}, so the answer is: {num_translate_adv(word)}')
        word = (input('\nLets try one more time! \nEnter number from one to ten or quite to exit: '))
    else:
        print(f'Russian word for {word} is: {num_translate_adv(word)}')
        word = (input('\nNice, lets try one more time! \nEnter number from one to ten or quite to exit: '))
