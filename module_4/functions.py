from library.library import ModuleCollections, ModuleString

module_2 = ModuleCollections(0,10,1,5)

input_str = """
homEwork:
  tHis iz your homeWork, copy these Text to variable.
  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

module_3 = ModuleString(input_str, r"( +iz +)", r" is ")
