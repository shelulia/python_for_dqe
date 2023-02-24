# Description
# homEwork:
#   tHis iz your homeWork, copy these Text to variable.
#  
#   You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
#  
#   it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
#  
#   last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.

import re
# put text to variable
input_str = """homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# Normalize text and create new sentence
# declare new variables to contein normalized string and new sentence
new_string = ""
new_sentence = ""
# divide text to sentences
for i in re.split(r'[\.]+', input_str.lower()):
    try:
        # define where first word starts
        first_word_index = re.search(r'([a-z])', i).start()
        # collecting last words from sentences to new sentence
        new_sentence = new_sentence + i.rsplit(' ', 1)[1] + " "
        if first_word_index == 0:
            # if sentence starts with word - put it to new_string variable
            # and capitalize
            new_string = new_string + i.capitalize() + "."
        else:
            # if sentence starts not word -
            # add it to new_string variable and capitalize first character
            new_string = new_string + i[0:first_word_index] \
                         + i[first_word_index:].capitalize() + "."
    except AttributeError:
        # if it is just new line - put it into new string variable
        new_string = new_string + i
        continue

# capitalize first word in new sentence and add it to the end of paragraph
new_sentence = new_sentence[:-1].capitalize() + "."
new_string = new_string + " " + new_sentence

# replace typo IZ with is
new_string = re.sub(r"( +iz +)", r" is ", new_string)
print(new_string)

# count number of spaces and non whitespace characters
count = sum(1 for match in re.finditer(r'[\S]+', new_string))
print(f"\nNumber of Spaces : {count}")
