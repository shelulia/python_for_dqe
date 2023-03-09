import random
import string
import re

class BaseMethods:
    """
    Class contains methods that were used in module 2
    """

    def decorate_list_of_dicts_generation(generate_random_list_of_dicts):
        """
        Decorator that calls function to create random list of dictionaries
        """
        def wrapper(*args, **kwargs):
            print("*" * 20 + " Generate a list of dict(s) " + "*" * 20 + "\n")
            a = generate_random_list_of_dicts(*args, **kwargs)
            print(f"Generated list of dicts:\n{a}\n")
            return a
        return wrapper


    @decorate_list_of_dicts_generation
    def generate_random_list_of_dicts(self, range_min, range_max, min_num_of_dicts, max_num_of_dicts):
        """
        Method to generate a list of random dictionaries
        :param range_min: minimal value for dictionary
        :param range_max: maximum value for dictionary
        :param min_num_of_dicts: minimum count of dictionaries
        :param max_num_of_dicts: maximum count of dictionaries
        :return: generated list of dictionaries
        """
        generated_list = [
            {random.choice(string.ascii_lowercase): random.randint(range_min, range_max) for _ in range(random.randint(min_num_of_dicts, max_num_of_dicts))}
            for _ in range(random.randint(min_num_of_dicts, max_num_of_dicts))
        ]

        return generated_list

    def get_list_of_dict_keys(self, list_of_dictionaries):
        """
        Method to define key(s) in dictionary
        :param list_of_dictionaries: list of dictionaries
        :returns common_keys: list of keys that are same in list_of_dictionaries
        """
        # create empty list to keep common keys
        list_of_keys = []
        for dict in list_of_dictionaries:
            for key, v in dict.items():
                list_of_keys.append(key)
        common_keys = list(set([i for i in list_of_keys if list_of_keys.count(i) >= 2]))

        return common_keys

    def decorate_common_dictionary(create_common_dictionary_from_several):
        """
        Decorator that calls function to create random list of dictionaries
        """
        def wrapper(*args, **kwargs):
            common_dict = create_common_dictionary_from_several(*args, **kwargs)
            return common_dict
        return wrapper


    @decorate_common_dictionary
    def create_common_dictionary_from_several(self, list_of_dicts, common_keys):
        """
        Method to collect all dictionaries to one
        :param list_of_dicts:
        :param common_keys:
        :return:
        """
        common_dict = {}
        for k in common_keys:
        # create empty list to collect values from key.
        # There might be cases when key exists in several(not all) dicts
            values_coll = []
            for dict in list_of_dicts:
                try:
                    values_coll.append([dict[k]])
                except KeyError:
                    pass
            # calculate max value for key
            max_val = int(''.join(str(el) for el in max(values_coll)))
            # start loop to identify in which dict max value for key exists
            # and generate new key name
            for dict in list_of_dicts:
            # There might be cases when key exists in several(not all) dicts
                try:
                    if dict[k] == max_val:
                        key_name = f"{k}_{list_of_dicts.index(dict) + 1}"
                        # append mav value with new named key to common dict
                        common_dict[key_name] = dict[k]
                    # remove key from dict
                    dict.pop(k)
                except KeyError:
                     pass
        # append left key-values from list of dict to common dict
        for dict in list_of_dicts:
            common_dict.update(dict)
        print(f"Common dictionary:\n{common_dict}")

    def text_normalization(self, input_text):
        """
        Method that normalize text to a normal case
        :param input_text: input text
        :return: norm_text: normalized text
        """
        # declare new variables to contain normalized string
        norm_text = ""
        # divide text to sentences
        for i in re.split(r'[\.]+', input_text.lower()):
            try:
                i = re.sub("\n+[\s]+", "\n", i)
                # define where first word starts
                first_word_index = re.search(r'([a-z])', i).start()
                if first_word_index == 0:
                    # if sentence starts with word - put it to new_string variable
                    # and capitalize
                    norm_text = norm_text + i.capitalize() + "."
                else:
                    # if sentence starts not word -
                    # add it to new_string variable and capitalize first character
                    norm_text = norm_text + i[0:first_word_index] \
                                 + i[first_word_index:].capitalize() + "."
            except AttributeError:
                # if it is just new line - put it into new string variable
                norm_text = norm_text + i
                continue
        return norm_text

    def create_last_words_sentence(self, input_text):
        """
        Method that creates a sentence out of last words from text
        :param input_text: input text
        :return: last_words_sentence: a sentence out of last words from text
        """
        last_words_sentence = ""
        for i in re.split(r'[\.]+', input_text.lower()):
            try:
                i = re.sub("\n+[\s]+", "\n", i)
                # print(i)
                last_words_sentence = last_words_sentence + i.rsplit(' ', 1)[1] + " "
            except Exception:
                continue
        last_words_sentence = last_words_sentence[:-1].capitalize() + "."
        return last_words_sentence

    def text_decorator_with_fixed_typos(replace_typo):
        """
        Decorator that displays fixed text
        """

        def wrapper(*args, **kwargs):
            fixed_text = replace_typo(*args, **kwargs)
            print(f"\n{fixed_text}")
        return wrapper

    @text_decorator_with_fixed_typos
    def replace_typo(self, input_text, typo, replacement):
        """
        Method that replaces typos in text
        :param input_text: text with typos
        :param typo: typo
        :param replacement: text that will replace typos
        :return: fixed text
        """
        print(f"\n\n" + "*" * 20 + f" Input text possibly contains typos {typo} that will be replaced with {replacement} "+ "*" * 20 + "\n")
        return re.sub(typo, replacement, input_text)

    def number_of_spaces_and_whitespaces(self, input_text):
        """
        Method that counts number of spaces/whitespaces in text
        :param input_text: input text
        :return: number of spaces/whitespaces
        """
        return len(re.findall('\s', input_text))

class ModuleCollections(BaseMethods):
    """
    Class that contains base methods for Module 2 'Collections'
    """

    def __init__(self, range_min, range_max, min_num_of_dicts, max_num_of_dicts):

        self.range_min = range_min
        self.range_max = range_max
        self.min_num_of_dicts = min_num_of_dicts
        self.max_num_of_dicts = max_num_of_dicts

        self.rand_list = self.generate_random_list_of_dicts(self.range_min, self.range_max, self.min_num_of_dicts, self.max_num_of_dicts)
        self.comm_keys = self.get_list_of_dict_keys(self.rand_list)
        if self.comm_keys:
            print(f"There are common keys in list of dicts: {self.comm_keys}")
            self.create_common_dictionary_from_several(self.rand_list, self.comm_keys)
        else:
            print("There are no common keys in list of dicts")


class ModuleString(BaseMethods):
    """
    Class that contains base methods for Module 3 'Strings'
    """

    def __init__(self, input_text, typo, replacement):

        self.input_text = input_text
        self.typo = typo
        self.replacement = replacement

        self.normalized_text = self.text_normalization(self.input_text)
        self.new_sent = self.create_last_words_sentence(self.input_text)
        self.new_text = self.normalized_text + self.new_sent
        self.fix_text = self.replace_typo(self.new_text, self.typo, self.replacement)
        print(f"\nNumber of Spaces : {self.number_of_spaces_and_whitespaces(self.input_text)}")
