import os
import sys
import json
import time
from datetime import datetime

sys.path.append("./module_5.oop_classes_addition.py")
sys.path.append("./module_7.csv_module.py")
from module_5.oop_classes_addition import CommonMethods, PdqeNewsPaperSite
from module_7.csv_module import AnalyzeNews, CsvTransformation

class JsonTransformation(PdqeNewsPaperSite):
    """
        Class contains methods to work with json files
    """
    def __init__(self):
        super().__init__()

    def if_valid_json_format(self, json_file):
        """
        Method that validates if json file has required format
        :param json_file: path to json file
        :return: list of dictionaries with valid format
        """
        self.input_dict = json.load(open(json_file, "r"))
        new_dict = []
        for elem in self.input_dict:
            if [k for k, v in elem.items()] == ["section", "text", "city"]:
                if elem["section"] == "news":
                    new_dict.append(elem)
            elif [k for k, v in elem.items()] == ["section", "text", "expiration_date"]:
                if elem["section"] == "ads":
                    try:
                        datetime.strptime((elem["expiration_date"]), "%Y-%m-%d").date()
                        new_dict.append(elem)
                    except:
                        pass
        if not new_dict:
            print(f"\nInput json file {json_file} doesn't match requirements on structure.")
        if len(self.input_dict) != len(new_dict):
            print(f"\nInput json file {json_file} will be partially processed an not all data meets requirements.")
        else:
            print(f"\nInput json file {json_file} will be fully processed")

        return new_dict

class AddJsonData(AnalyzeNews):
    def __init__(self, output_file="./newspaper.txt", input_file="../module_6/test_message.txt"
                 , word_count_file_path="./word_count.csv", analyze_text_csv="./text_analysys.csv"
                 , input_json_file = "./json_message.json"):
        self.file_to_read = output_file
        self.input_file_name = input_file
        self.word_count_file_path = word_count_file_path
        self.analyze_text_csv = analyze_text_csv
        self.input_json_file = input_json_file

        self.csv_transf = CsvTransformation()

        sys.path.append(output_file)
        sys.path.append(input_file)
        sys.path.append(word_count_file_path)
        sys.path.append(analyze_text_csv)
        sys.path.append(input_json_file)

        self.json_transf = JsonTransformation()

    def get_category(self):
        """
        Method to get category for user's input
        :return:
        """
        print("""\nPlease choose category for your message:
                   1 - News
                   2 - Advertising
                   3 - Check your luck
                   4 - Add data from your txt file
                   5 - Add data from your json file
                   6 - Exit""")
        self.val = input("\nEnter your value: ")
        return self.val

    def user_input(self):
        """
        Method to populate file with user's data
        """

        val = 0
        while True:
            val = self.get_category()

            if int(val) == 1:
                title = f"\n" + "*" * 20 + f" News " + "*" * 20
                self.news_text, self.news_city = self.news.get_news()
                self.common_methods.populate_output_file(title,
                                                         f"News: {self.news_text}",
                                                         f"City: {self.news_city}",
                                                         f"Publish date: {self.common_methods.get_current_date()}",
                                                         f"{self.file_to_read}")

            elif int(val) == 2:
                title = f"\n" + "*" * 20 + f" Private Ads " + "*" * 20
                self.ads_text, self.expiration_date = self.ads.get_ads()
                self.common_methods.populate_output_file(title,
                                                         f"Ads: {self.ads_text}",
                                                         f"Expiration date: {self.expiration_date}",
                                                         f"Days left: {self.ads.get_days_left(str(self.expiration_date))}",
                                                         f"{self.file_to_read}")


            elif int(val) == 3:
                title = f"\n" + "*" * 20 + f" Check your luck " + "*" * 20
                self.user_choise = self.luck.get_user_number()
                self.randomed = self.luck.get_random_int()
                self.common_methods.populate_output_file(title,
                                                         f"Your choice: {self.user_choise}",
                                                         f"System choice: {self.randomed}",
                                                         f"Result: {self.luck.success_of_fail(self.user_choise, self.randomed)}",
                                                         f"{self.file_to_read}")

            elif int(val) == 4:
                try:
                    txt = self.read_input_file(self.input_file_name)
                    for lst in txt:
                        section = self.validate_if_date(lst)
                        if section == 1:
                            title = f"\n" + "*" * 20 + f" Private Ads " + "*" * 20
                            self.ads_text = self.base_methods.text_normalization(" ".join(lst[:-1]))
                            self.expiration_date = lst[-1]
                            self.common_methods.populate_output_file(title,
                                                                     f"Ads: {self.ads_text}",
                                                                     f"Expiration date: {self.expiration_date}",
                                                                     f"Days left: {self.ads.get_days_left(str(self.expiration_date))}",
                                                                     f"{self.file_to_read}")
                        else:
                            title = f"\n" + "*" * 20 + f" News " + "*" * 20
                            self.news_text = self.base_methods.text_normalization(" ".join(lst[:-1]).strip())
                            self.news_city = " ".join(lst[-1:]).strip()
                            self.common_methods.populate_output_file(title,
                                                                     f"News: {self.news_text}",
                                                                     f"City: {self.news_city}",
                                                                     f"Publish date: {self.common_methods.get_current_date()}",
                                                                     f"{self.file_to_read}")
                    os.remove(self.input_file_name)
                except Exception as e:
                    print(e)
                    print(f"FAILURE: file {self.input_file_name} wasn't processed. \nPlease try again.")

            elif int(val) == 5:
                try:
                    list_of_dicts = self.json_transf.if_valid_json_format(self.input_json_file)
                    if list_of_dicts:
                        for elem in list_of_dicts:
                            if elem["section"] == "news":
                                title = f"\n" + "*" * 20 + f" News " + "*" * 20
                                self.common_methods.populate_output_file(title,
                                                                         f"News: {elem['text']}",
                                                                         f"City: {elem['city']}",
                                                                         f"Publish date: {self.common_methods.get_current_date()}",
                                                                         f"{self.file_to_read}")
                            else:
                                title = f"\n" + "*" * 20 + f" Private Ads " + "*" * 20
                                self.common_methods.populate_output_file(title,
                                                                         f"Ads: {elem['text']}",
                                                                         f"Expiration date: {elem['expiration_date']}",
                                                                         f"Days left: {self.ads.get_days_left(str(elem['expiration_date']))}",
                                                                         f"{self.file_to_read}")
                        os.remove(self.input_json_file)
                    else:
                        print(
                            f"FAILURE: file {self.input_json_file} wasn't deleted as wasn't processed.")
                except Exception as e:
                    print(e)
                    print(f"FAILURE: file {self.input_json_file} wasn't processed. \nPlease try again. File wasn't deleted.")

            elif int(val) == 6:
                print("Thanks for your time. Have a nice day!")
                break
            else:
                print(f"Please select appropriate category 1, 2, 3, 4, 5, 6")
                continue

        print(f"Please find results in {self.file_to_read}")

        time.sleep(3)
        self.csv_transf.write_to_csv(self.file_to_read, ['word', 'count'], self.word_count_file_path, "word_analysis")
        self.csv_transf.write_to_csv(self.file_to_read, ["letter", "count", "uppercase_count", "percentage"]
                                     , self.analyze_text_csv, "letter_analysis")

