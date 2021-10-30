import string


class Day4:

    def split_words(initial_list: list):
        new_list = []

        for item in initial_list:
            list_to_append = item.split()
            new_list = new_list + list_to_append
        return new_list

    def find_parasites(text: str, max_amount: int):
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))  # removing punctuation marks
        text_list = text.split()  # splitting string by spaces and converting to the list
        result = {}

        for word in text_list:  # counting words and adding them to dictionary if count exceeds max_amount
            number_of_words = text_list.count(word)
            if number_of_words >= max_amount:
                result[word] = number_of_words

        return result
