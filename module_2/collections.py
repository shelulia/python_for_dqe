import random
import _collections as c

print("=" * 50 + " Module 2 " + "=" * 50 + "\n")
#Sub-task 1
print("*" * 20 + " Generate a list of 3 dicts " + "*" * 20 + "\n")

#declare iterator and empty list
elem_num_iter = 0
generated_list = []
#start loop to create a list of 3 dicts
while elem_num_iter < 3:
    i = 0
    mydict = {}
    #start loop to generate a dict of 5 pairs: key-value
    while i < 5:
        key = str(chr(random.randint(ord('a'), ord('z'))))
        value = random.randrange(0, 100)
        mydict.update({key: value})
        i+=1
    generated_list.append(mydict)
    elem_num_iter += 1
#display generated list of dicts
print(f"Generated list of dicts:\n{generated_list}\n")

#Sub-task 2
print("*" * 20 + " Combine dicts from list to 1 dict" + "*" * 20 + "\n")

#define common keys
#create empty list to keep common keys
p = []
for dict in generated_list:
    for key, v in dict.items():
        p.append(key)
common_keys = list(set([i for i in p if p.count(i) >= 2]))

#display common keys and collect all dicts to one
if common_keys:
    print(f"There are common keys in list of dicts: {common_keys}")
    # Create empty dict to combine all dicts from list there
    common_dict = {}
    for k in common_keys:
        #create empty list to collect values from key. There might be cases when key exists in several(not all) dicts
        values_coll = []
        for dict in generated_list:
            try:
                values_coll.append([dict[k]])
            except:
                pass
        #calculate max value for key
        max_val = int(''.join(str(el) for el in max(values_coll)))
        #start loop to identify in which dict max value for key exists and generate new key name
        for dict in generated_list:
            #There might be cases when key exists in several(not all) dicts
            try:
                if dict[k] == max_val:
                    key_name = f"{k}_{generated_list.index(dict)}"
                    #append mav value with new named key to common dict
                    common_dict[key_name] = dict[k]
                #remove key from dict
                dict.pop(k)
            except:
                pass
    #append left key-values from list of dict to common dict
    for dict in generated_list:
        common_dict.update(dict)
    print(f"Common dictionary:\n{common_dict}")
else:
    print(f"There are no common keys in list of dicts")

#
#
# print(common_dict)
# # generated_list
# # i = 0
# # while i < len(generated_list):
# #     first_dict = generated_list[i]
# #     second_dict = generated_list[i+1]



# c = {'a': 5, 'b': 7, 'g': 11, 'd':0}
# d = {'a': 3, 'c': 35, 'g': 42, 'e':30}
#
# common_dict = {}
#
# intersect = (c.keys() & d.keys())
# for k in intersect:
#     if c[k] >= d[k]:
#         key_name = k + '_1'
#         common_dict[key_name] = c[k]
#     else:
#         key_name = k + '_2'
#         common_dict[key_name] = d[k]
#     c.pop(k)
#     d.pop(k)
# common_dict.update(c)
# common_dict.update(d)
# print(common_dict)


c = {'a': 5, 'b': 7, 'g': 11, 'd':0}
d = {'a': 3, 'c': 35, 'g': 42, 'e':30}
e = {'d': 3, 'f': 35, 'k': 42, 'u':30}
dicts = [{'a': 5, 'b': 7, 'g': 11, 'd':0},{'d': 3, 'a': 35, 'k': 42, 'u':30},{'a': 3, 'c': 35, 'g': 42, 'e':30}]

seq = [max([x['a'] for x in dicts])]
# print(seq)

# for elem in dicts:
#     if [elem['g']] == [max([x['g'] for x in dicts])] :
#         print(dicts.index(elem))

# for elem in dicts:
#     for key, v in elem.items():
#         p.append(key)
# output = [list(set([i for i in p if p.count(i) >= 2]))]
# print(output)





# for elem in dicts:
#     if [elem['g']] == [max([x['g'] for x in dicts])] :
#         print(dicts.index(elem))