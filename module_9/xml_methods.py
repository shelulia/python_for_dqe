import os
import sys
import time
import xml.etree.ElementTree as E

from module_4.library.library import BaseMethods
from module_7.csv_module import CsvTransformation
from module_8.json_methods import JsonTransformation, AddJsonData

sys.path.append("./module_7.csv_module.py")
sys.path.append("./module_8.json_methods.py")
sys.path.append("./module_4.library.library.py")
sys.path.append("./module_5.oop_classes_addition.py")

class XmlTransformation(JsonTransformation):
    """
    Class contains methods to transform xml files
    """
    def __init__(self):
        super().__init__()

    def convert_xml_to_required_dict(self, xml_file_name):
        """
        Method that reads data from xml file and convert it to required format of dictionary
        :param xml_file: input xml file
        :return: list of dictionaries
        """

        xml_file = E.parse(xml_file_name)
        root = xml_file.getroot()

        xml_list = []

        try:
            for section in root:
                nested_dict= {}
                if section.get("name") in ["news", "ads"]:
                    nested_dict["section"] = section.get("name")
                    for subsection in section:
                        nested_dict[subsection.tag] = subsection.text
                    xml_list.append(nested_dict)
        except:
            print(f"Input {xml_file_name} doesn't meet the requirements. Please follow clues on structure."
                  f"\nFile wasn't processed.")

        return xml_list

class AddXmlData(AddJsonData):
    def __init__(self, output_file="./newspaper.txt", input_file="../module_6/test_message.txt"
                 , word_count_file_path="./word_count.csv", analyze_text_csv="./text_analysis.csv"
                 , input_json_file="../module_8/json_message.json", input_xml_file="./xml_message.xml"):
        self.file_to_read = output_file
        self.input_file_name = input_file
        self.word_count_file_path = word_count_file_path
        self.analyze_text_csv = analyze_text_csv
        self.input_json_file = input_json_file
        self.input_xml_file = input_xml_file

        self.csv_transf = CsvTransformation()

        sys.path.append(output_file)
        sys.path.append(input_file)
        sys.path.append(word_count_file_path)
        sys.path.append(analyze_text_csv)
        sys.path.append(input_json_file)
        sys.path.append(input_xml_file)

        self.json_transf = JsonTransformation()
        self.xml_transf = XmlTransformation()
        self.base_methods = BaseMethods()

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
                           6 - Add data from your xml file
                           7 - Exit""")
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
                    list_of_dicts = self.json_transf.if_valid_json_format(
                        self.json_transf.read_json(self.input_json_file), self.input_json_file)
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
                    print(
                        f"FAILURE: file {self.input_json_file} wasn't processed. \nPlease try again. File wasn't deleted.")

            elif int(val) == 6:
                try:
                    xml_lst = self.xml_transf.convert_xml_to_required_dict(self.input_xml_file)
                    list_of_dicts = self.json_transf.if_valid_json_format(xml_lst, self.input_xml_file)
                    if list_of_dicts:
                        for elem in list_of_dicts:
                            if elem["section"] == "news":
                                title = f"\n" + "*" * 20 + f" News " + "*" * 20
                                self.common_methods.populate_output_file(title,
                                                                         f"News: {elem['text']}",
                                                                         f"City: {elem['city']}",
                                                                         f"Publish date: {self.common_methods.get_current_date()}",                                                                             f"{self.file_to_read}")
                            else:
                                title = f"\n" + "*" * 20 + f" Private Ads " + "*" * 20
                                self.common_methods.populate_output_file(title,
                                                                         f"Ads: {elem['text']}",
                                                                         f"Expiration date: {elem['expiration_date']}",
                                                                         f"Days left: {self.ads.get_days_left(str(elem['expiration_date']))}",
                                                                         f"{self.file_to_read}")
                        os.remove(self.input_xml_file)
                    else:
                        print(
                            f"FAILURE: file {self.input_xml_file} wasn't deleted as wasn't processed.")

                except Exception as e:
                    print(e)
                    print(
                        f"FAILURE: file {self.input_xml_file} wasn't processed. \nPlease try again. File wasn't deleted.")

            elif int(val) == 7:
                print("Thanks for your time. Have a nice day!")
                break
            else:
                print(f"Please select appropriate category 1, 2, 3, 4, 5, 6, 7")
                continue

        print(f"Please find results in {self.file_to_read}")

        time.sleep(3)
        self.csv_transf.write_to_csv(self.file_to_read, ['word', 'count'], self.word_count_file_path, "word_analysis")
        self.csv_transf.write_to_csv(self.file_to_read, ["letter", "count", "uppercase_count", "percentage"]
                                     , self.analyze_text_csv, "letter_analysis")
