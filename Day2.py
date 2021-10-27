import json


class Day2:

    def text_func(text: str, max_len: int):

        symbols_with_spaces = len(text)
        symbols_no_spaces = len(text.replace(' ', ''))

        symbols_even = symbols_with_spaces % 2 == 0
        print(f'Kоличество символов в тексте {symbols_with_spaces}')
        print(f'Kоличество символов без учета пробелов {symbols_no_spaces}')
        if symbols_even:
            print('Kоличество символов в тексте четное')
        else:
            print('Kоличество символов в тексте нечетное')
        if symbols_with_spaces > max_len:
            print(f'Длина текста превышает длину {max_len} символов')

    def text_processor(text: str, max_len: int, forbidden_words: list):

        pure_text = text

        for word in forbidden_words:
            pure_text = pure_text.replace(word, '***')

        if len(pure_text) <= max_len:
            pure_short_text = pure_text[:max_len]
        else:
            pure_short_text = pure_text[:max_len] + '...'

        dictionary = {"length": len(text),
                      "pure_length": len(text.replace(' ', '')),
                      "origin_text": text,
                      "pure_text": pure_text,
                      "pure_short_text": pure_short_text
                      }
        json_object = json.loads(json.dumps(dictionary))

        print(json_object)
