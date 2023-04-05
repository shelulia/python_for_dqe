import sys
sys.path.append("./module_7/csv_module.py")
from module_8.json_methods import AddJsonData

# PLease add parameters  to AddJsonData if required
# output_file default "./newspaper.txt"
# input_file txt default "../module_6/test_message.txt"
# word_count_file_path default "./word_count.csv"
# analyze_text_csv default "./text_analysys.csv"
# input_json_file default  "./json_message.json"

# format for JSON file:
# [{"section": "news", "text": "some text", "city": "some city"}
# , {"section": "ads", "text": "some text", "expiration_date": "some date in format yyyy-mm-dd"}]
# Please note if file at partially meets the requirements - allowed data will be processed

module_8 = AddJsonData()
module_8.user_input()


