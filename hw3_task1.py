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


def num_translate(i):
    """Func returns value from dict {words}"""
    return words.get(i)


word = (input('Hello, welcome to the translator from English to Russian!\n'
              '!Pls enter number from one to ten or quite to exit: '))
while True:
    if word == 'quite':
        print('Thanks and goodbye!')
        break
    elif word not in words.keys():
        print(f'I\'m sry, I don\'t know word: {word}, so the answer is: {num_translate(word)}')
        word = (input('Lets try one more time! \nEnter number from one to ten or quite to exit: '))
    else:
        print(f'Russian word for: {word} is: {num_translate(word)}')
        word = (input('Nice, lets try one more time! \nEnter number from one to ten or quite to exit: '))
