import os
import sys
import time

import pyodbc

from library import BaseMethods
from module_7.csv_module import CsvTransformation
from module_8.json_methods import JsonTransformation
from module_9.xml_methods import AddXmlData, XmlTransformation


class DbTransformation:
    def __init__(self, db_name = "test.db"):
        self.connection = pyodbc.connect("DRIVER={SQLite};Direct=True;"
                                         f"Database={db_name};"
                                         f"ansi=True;autocommit=True")
        self.connection.setdecoding(pyodbc.SQL_CHAR, encoding='UTF-8')
        self.connection.setdecoding(pyodbc.SQL_WCHAR, encoding='UTF-8')
        self.connection.setencoding(encoding='UTF-8')

    def insert_into_db(self, table_name, data):
        with self.connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO {table_name} VALUES{data};")

    def select_from_table(self, table_name):
        with self.connection.cursor() as cursor:
            if table_name == "news":
                cursor.execute("CREATE TABLE IF NOT EXISTS News (news text, city text, publish_date text)")

            if table_name == "ads":
                cursor.execute("CREATE TABLE IF NOT EXISTS Ads (ads text, expiration_date text, days_left int)")

            if table_name == "luck":
                cursor.execute(
                        "CREATE TABLE IF NOT EXISTS Luck (your_choice int, system_choise int, result text)")

            result = cursor.execute(f"SELECT * FROM {table_name};")
            rows = result.fetchall()
            data = [tuple(row) for row in rows]
            return(data)

    def deduplicate(self, table_name,  data):
        with self.connection:
            existing_set = self.select_from_table(table_name)

            if len(existing_set)>0:
                new_data_validation = [x for x in [data] if x not in existing_set]
                if new_data_validation:
                    print(f"New data will be inserted: {new_data_validation}")
                    self.insert_into_db(table_name,  str(new_data_validation).strip('[]'))
                else:
                    print("ATTENTION: same data exists in table and won't be inserted")
            else:
                print("All data will be inserted")
                self.insert_into_db(table_name, data)

class AddDataToDatabase(AddXmlData):
    def __init__(self, output_file="./newspaper.txt", input_file="../module_6/test_message.txt"
                 , word_count_file_path="./word_count.csv", analyze_text_csv="./text_analysis.csv"
                 , input_json_file="../module_8/json_message.json", input_xml_file="../module_9/xml_message.xml"
                 , db_name = "test.db"):
        self.file_to_read = output_file
        self.input_file_name = input_file
        self.word_count_file_path = word_count_file_path
        self.analyze_text_csv = analyze_text_csv
        self.input_json_file = input_json_file
        self.input_xml_file = input_xml_file
        self.db_name = db_name

        self.csv_transf = CsvTransformation()
        self.db_methods = DbTransformation(self.db_name)

        sys.path.append(output_file)
        sys.path.append(input_file)
        sys.path.append(word_count_file_path)
        sys.path.append(analyze_text_csv)
        sys.path.append(input_json_file)
        sys.path.append(input_xml_file)
        sys.path.append(db_name)

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
                self.db_methods.deduplicate("news", (self.news_text, self.news_city, str(self.common_methods.get_current_date())))

            elif int(val) == 2:
                title = f"\n" + "*" * 20 + f" Private Ads " + "*" * 20
                self.ads_text, self.expiration_date = self.ads.get_ads()
                self.common_methods.populate_output_file(title,
                                                         f"Ads: {self.ads_text}",
                                                         f"Expiration date: {self.expiration_date}",
                                                         f"Days left: {self.ads.get_days_left(str(self.expiration_date))}",
                                                         f"{self.file_to_read}")
                self.db_methods.deduplicate("ads", (
                self.ads_text, self.expiration_date, self.ads.get_days_left(str(self.expiration_date))))

            elif int(val) == 3:
                title = f"\n" + "*" * 20 + f" Check your luck " + "*" * 20
                self.user_choise = self.luck.get_user_number()
                self.randomed = self.luck.get_random_int()
                self.common_methods.populate_output_file(title,
                                                         f"Your choice: {self.user_choise}",
                                                         f"System choice: {self.randomed}",
                                                         f"Result: {self.luck.success_of_fail(self.user_choise, self.randomed)}",
                                                         f"{self.file_to_read}")
                self.db_methods.deduplicate("luck", (
                    self.user_choise, self.randomed, self.luck.success_of_fail(self.user_choise, self.randomed)))

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
                            self.db_methods.deduplicate("ads", (
                                self.ads_text, self.expiration_date, self.ads.get_days_left(str(self.expiration_date))))

                        else:
                            title = f"\n" + "*" * 20 + f" News " + "*" * 20
                            self.news_text = self.base_methods.text_normalization(" ".join(lst[:-1]).strip())
                            self.news_city = " ".join(lst[-1:]).strip()
                            self.common_methods.populate_output_file(title,
                                                                     f"News: {self.news_text}",
                                                                     f"City: {self.news_city}",
                                                                     f"Publish date: {self.common_methods.get_current_date()}",
                                                                     f"{self.file_to_read}")
                            self.db_methods.deduplicate("news", (
                            self.news_text, self.news_city, str(self.common_methods.get_current_date())))
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
                                self.db_methods.deduplicate("news", (
                                elem['text'], elem['city'], str(self.common_methods.get_current_date())))
                            else:
                                title = f"\n" + "*" * 20 + f" Private Ads " + "*" * 20
                                self.common_methods.populate_output_file(title,
                                                                         f"Ads: {elem['text']}",
                                                                         f"Expiration date: {elem['expiration_date']}",
                                                                         f"Days left: {self.ads.get_days_left(str(elem['expiration_date']))}",
                                                                         f"{self.file_to_read}")
                                self.db_methods.deduplicate("ads", (
                                    elem['text'], elem['expiration_date'],
                                    self.ads.get_days_left(str(elem['expiration_date']))))
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
                                                                         f"Publish date: {self.common_methods.get_current_date()}",
                                                                         f"{self.file_to_read}")
                                self.db_methods.deduplicate("news", (
                                elem['text'], elem['city'], str(self.common_methods.get_current_date())))
                            else:
                                title = f"\n" + "*" * 20 + f" Private Ads " + "*" * 20
                                self.common_methods.populate_output_file(title,
                                                                         f"Ads: {elem['text']}",
                                                                         f"Expiration date: {elem['expiration_date']}",
                                                                         f"Days left: {self.ads.get_days_left(str(elem['expiration_date']))}",
                                                                         f"{self.file_to_read}")
                                self.db_methods.deduplicate("ads", (
                                    elem['text'], elem['expiration_date'],
                                    self.ads.get_days_left(str(elem['expiration_date']))))
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


