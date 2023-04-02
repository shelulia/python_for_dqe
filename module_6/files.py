import sys
sys.path.append("./module_5/oop_classes_addition.py")
from module_5.oop_classes_addition import PdqeNewsPaperSite

# Note! please insert into parameter desired target and source file locations
# For source file please follow next rules:
# divide blocks with new line separator
# if you need to put Ads - please add date in last line in format YYYY-mm-dd
# if you need to put News - please add city

# if you need to put data from your own file, please populate object class
# PdqeNewsPaperSite with parameters(input_file, output_file)
# It has default values in case none parameters are passed

module_5 = PdqeNewsPaperSite()

inpt_file = module_5.user_input()


