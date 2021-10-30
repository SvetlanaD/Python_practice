import string


class Day3:
    az = string.ascii_letters  #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

    def coder2(text: str):
        text_coded = ''

        for i in range(len(text)):
            symbol = text[i]
            symbol_coded = Day3.change_case(symbol)

            if symbol in Day3.az:
                index_in_az = Day3.az.index(symbol_coded)
                if index_in_az in [25, 51]:  # indexes of z and Z
                    symbol_coded = Day3.az[index_in_az - 25]
                else:
                    symbol_coded = Day3.az[index_in_az + 1]

            text_coded = text_coded + symbol_coded

        print(text_coded)

    def decoder2(text: str):
        text_decoded = ''

        for i in range(len(text)):
            symbol = text[i]
            symbol_coded = Day3.change_case(symbol)

            if symbol in Day3.az:
                index_in_az = Day3.az.index(symbol_coded)
                if index_in_az in [0, 26]:  # indexes of a and A
                    symbol_coded = Day3.az[index_in_az + 25]
                else:
                    symbol_coded = Day3.az[index_in_az - 1]

            text_decoded = text_decoded + symbol_coded

        print(text_decoded)

    def change_case(c: str):
        if c.islower():
            result = c.upper()
        else:
            result = c.lower()

        return result
