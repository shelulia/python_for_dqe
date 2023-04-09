import sys
sys.path.append("./module_10/db_methods.py")
from module_10.db_methods import AddDataToDatabase, DbTransformation
# Please add parameters  to AddJsonData if required
# output_file default "./newspaper.txt"
# input_file txt default "../module_6/test_message.txt"
# word_count_file_path default "./word_count.csv"
# analyze_text_csv default "./text_analysis.csv"
# input_json_file default  "../module_8/json_message.json"
# input_xml_file default "./xml_message.xml"
# database_name default "test.db"

# format for JSON file:
# [{"section": "news", "text": "some text", "city": "some city"}
# , {"section": "ads", "text": "some text", "expiration_date": "some date in format yyyy-mm-dd"}]
# Please note if file at partially meets the requirements - allowed data will be processed

# format for XML file:
# <root>
#     <section name="news">
#         <text>some interesting news here</text>
#         <city>Fantastic City</city>
#     </section>
#     <section name="ads">
#         <text>buy 3 pay 2</text>
#         <expiration_date>2023-05-10</expiration_date>
#     </section>
# ... </root>

module_10= AddDataToDatabase()
module_10.user_input()

# Note: to validate results please uncomment 4 next lines:
# module_10_check = DbTransformation()
# print(module_10_check.select_from_table("news"))
# print(module_10_check.select_from_table("ads"))
# print(module_10_check.select_from_table("luck"))