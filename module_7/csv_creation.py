import sys
sys.path.append("./module_7/csv_module.py")
from module_7.csv_module import AnalyzeNews

# Note! please insert into parameters if required
# 1. output_file - file with written user data. default "./newspaper.txt",
# input_file - file that contains many user inputs. Default "../module_6/test_message.txt"
# word_count_file_path - path to csv file to with counted words.Default "./word_count.csv",
# analyze_text_csv - path to csv file to with counted letters. Default  "./text_analysis.csv"

module_7 = AnalyzeNews()