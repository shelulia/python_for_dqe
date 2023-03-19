from datetime import date, datetime
import random

class CommonMethods:
    """
    Class contains common methods
    """
    def __create_output_file__(self, output_file):
        """
        Method to create output file
        """
        if not output_file:
            open(output_file, 'a').close()

    def populate_output_file(self, title, section_text, city_exp_date, calculated_val, output_file='/Users/shaliyu1/Documents/python_for_dqe/module_5/PDQE_newspaper.txt'):
        self.__create_output_file__(output_file)
        with open(output_file, "a") as myfile:
            myfile.write(
                f" {title} " + f"\n{section_text}" + f"\n{city_exp_date}" + f"\n{calculated_val}")

    def get_current_date(self):
        """
        Method that returns current date
        :return: current date
        """
        today = date.today()
        return today


class News:
    """
    Class contains methods related to News section
    """

    def get_news(self):
        """
        Method to get news and city from user
        :return: news and city
        """
        print("\nNews will be added to next edition")
        news = input("""\nPlease enter your news: """)
        news_city = input("""\nPlease enter your city: """)
        return news, news_city

class Ads(CommonMethods):
    """
    Class contains methods related to advertisement section
    """

    common_methods = CommonMethods()

    def get_ads(self):
        """
        Method to get input regarding ads fron user
        :return: ads text, expiration_date
        """
        print("\nAdvertising will be added to next edition")
        ads = input("""\nPlease enter your ads: """)
        expiration_date = input("""\nPlease enter expiration date in format 'yyyy-mm-dd': """)
        return ads, expiration_date

    def get_days_left(self, expiration_date):
        """
        Merhod to calculate how many days left before ads expired
        :param expiration_date: expiration_date
        :return: counted days left
        """
        date_format = "%Y-%m-%d"
        days_left = datetime.strptime(expiration_date, date_format).date() - self.common_methods.get_current_date()
        return days_left.days

class CheckYourLuck:
    """
    Entertaining for user to validate if he guessed the number
    """
    def get_random_int(self):
        """
        Method to generate random integer
        :return: generated integer from 0 to 10
        """
        return random.randint(0, 10)


    def get_user_number(self):
        """
        Method to get user's guessed number
        :return: user's guessed number
        """
        print("\nYour choice will be published in next edition")
        guess = input("""\nPlease enter your number from 0 to 10: """)
        return guess

    def success_of_fail(self,  guessed, randomed):
        """
        Method to compare if generated number matches with guessed
        :param guessed: user's guessed number
        :param randomed: generated number
        :return: message if guessed or not
        """
        if randomed == int(guessed):
            msg = "Yehoo! You're lucky today"
        else:
            msg = "Ohh, try another time"
        return msg


class PdqeNewsPaperSite(CommonMethods):
    """
    Class that gets information from user and puts it into txt file
    """

    def __init__(self, output_file):
        self.output_file_name = output_file

    news = News()
    ads = Ads()
    luck = CheckYourLuck()
    common_methods = CommonMethods()

    print("*" * 20 + f" Welcome to PDQE Newspaper site " + "*" * 20)
    print("""\nPlease choose category for your message:
            1 - News
            2 - Advertising
            3 - Check your luck""")

    def get_category(self):
        """
        Method to get category for user's input
        :return: 
        """
        val = input("\nEnter your value: ")
        return val

    def user_input(self):
        """
        Method to populate file with user's data
        """
        val = self.get_category()
        if int(val) == 1:
            title = f"\n" + "*" * 20 + f" News " + "*" * 20
            self.news_text, self.news_city = self.news.get_news()
            self.common_methods.populate_output_file(title,
                                                     f"News: {self.news_text}",
                                                     f"City: {self.news_city}",
                                                     f"Publish date: {self.common_methods.get_current_date()}",
                                                     f"{self.output_file_name}")

        elif int(val) == 2:
            title = f"\n" + "*" * 20 + f" Private Ads " + "*" * 20
            self.ads_text, self.expiration_date = self.ads.get_ads()
            self.common_methods.populate_output_file(title,
                                                     f"Ads: {self.ads_text}",
                                                     f"Expiration date: {self.expiration_date}",
                                                     f"Days left: {self.ads.get_days_left(str(self.expiration_date))}",
                                                     f"{self.output_file_name}")

        else:
            title = f"\n" + "*" * 20 + f" Check your luck " + "*" * 20
            self.user_choise = self.luck.get_user_number()
            self.randomed = self.luck.get_random_int()
            self.common_methods.populate_output_file(title,
                                                     f"Your choice: {self.user_choise}",
                                                     f"System choice: {self.randomed}",
                                                     f"Result: {self.luck.success_of_fail(self.user_choise, self.randomed)}",
                                                     f"{self.output_file_name}")

        print(f"Please find results in {self.output_file_name}")




