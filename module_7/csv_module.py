import re
import csv
import sys
import time

sys.path.append("./module_5.oop_classes_addition.py")
from module_5.oop_classes_addition import PdqeNewsPaperSite

class CsvTransformation():
    """
        Class contains methods to work with csv files
    """

    def remove_delimiters (self, input_string, delimiters = r"[\,\.\!\?\/\&\-\:\;\@\=\*]+"):
        """
        Method that removes any delimiters in string
        :param delimiters: list of delimiters
        :param input_string: sring to be transformed
        :return: string without delimiters
        """
        return re.sub(delimiters, "", input_string)

    def word_count(self, str):
        """
        Method that counts occurrence of each word in string
        :param str: string to be used
        :return: count of word occurrence
        """
        counts = dict()
        words = str.split()

        for word in words:
            word = self.remove_delimiters(word).title()
            #check if word is word, not digit or star - then count
            if re.findall(r'[\*\d+]', word) == []:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1

        return counts

    def remove_spaces(self, input_str):
        """
        Method to remove spaces and white characters from input string
        :param input_str: string to be transformed
        :return: transformed string
        """
        return re.sub(r"\s", "", input_str)

    def analyze_count_letters(self, input_str):
        """
        Method that counts occurrence if letter, count letter in upper case, percentage
        :param input_str: string to be analysed
        :return: res - dictionary of letters and counts
        """
        res = {i.lower(): [input_str.lower().count(i.lower())
            , (input_str.count(i) if i.isupper() else 0)
            , input_str.lower().count(i.lower()) / len(self.remove_spaces(input_str)) * 100]
               for i in set(self.remove_spaces(input_str))}
        return res

    def write_to_csv(self, file_to_read, headers, output_file, mode ):
        with open(file_to_read, "r") as f:
            contents = f.read()
            if mode == "word_analysis":
                contents_str = self.word_count(contents)
            elif mode == "letter_analysis":
                contents_str = self.analyze_count_letters(self.remove_delimiters(contents))
            else:
                print("Please specify word_analysis or letter_analysis mode")
            with open(output_file, "w") as csvfile:
                fieldnames = headers
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for k, v in contents_str.items():
                    writer.writerow(dict(zip(headers, [k] + [v] if type(v)!= list else [k] + v)))

class AnalyzeNews(PdqeNewsPaperSite):
    def __init__(self,  output_file = "./newspaper.txt", input_file = "../module_6/test_message.txt"
               , word_count_file_path = "./word_count.csv", analyze_text_csv = "./text_analysys.csv"):
        super().__init__()
        self.file_to_read = output_file
        self.input_file_name = input_file
        self.word_count_file_path = word_count_file_path
        self.analyze_text_csv = analyze_text_csv

        self.csv_transf = CsvTransformation()

        sys.path.append(output_file)
        sys.path.append(input_file)
        sys.path.append(word_count_file_path)
        sys.path.append(analyze_text_csv)

        PdqeNewsPaperSite(self.file_to_read, self.input_file_name)
        PdqeNewsPaperSite.user_input(self)
        time.sleep(3)
        self.csv_transf.write_to_csv(self.file_to_read, ['word', 'count'], self.word_count_file_path, "word_analysis")
        self.csv_transf.write_to_csv(self.file_to_read, ["letter", "count", "uppercase_count", "percentage"]
                                   , self.analyze_text_csv, "letter_analysis")
