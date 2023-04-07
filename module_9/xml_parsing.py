import sys
sys.path.append("./module_8/xml_parsing.py.py")

from module_9.xml_methods import AddXmlData

# PLease add parameters  to AddJsonData if required
# output_file default "./newspaper.txt"
# input_file txt default "../module_6/test_message.txt"
# word_count_file_path default "./word_count.csv"
# analyze_text_csv default "./text_analysis.csv"
# input_json_file default  "../module_8/json_message.json"
# input_xml_file default "./xml_message.xml"

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

module_9= AddXmlData()
module_9.user_input()


