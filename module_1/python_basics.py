import random

# Task
# Create a python script:
#
# create list of 100 random numbers from 0 to 1000
# sort list from min to max (without using sort())
# calculate average for even and odd numbers
# print both average result in console
# Each line of code should be commented with description.
#
# Commit script to git repository and provide link as home task result.

print("=" * 50 + " Module 1 " + "=" * 50 + "\n")
# Sub-task 1
print("*" * 20 + " Creation of list of 100 random numbers from 0 to 1000"
                 "is started " + "*" * 20 + "\n")
# Create empty list to put random numbers there
random_list = []
# declare step
st = 0
# start loop for putting random numbers
while st < 100:
    # append random numbers to the list
    random_list.append(random.randrange(0, 1000))
    # iterate
    st += 1

print(f"List of random numbers was created: \n{random_list}")

# Sub-task 2
print("\n" + "*" * 20 + " Sorting the list of random numbers is "
      "started " + "*" * 20 + "\n")
# create empty list to keep there sorted values
sorted_list = []
# start loop for sorting values
while random_list:
    # pick up min value from list, put to new list
    sorted_list.append(min(random_list))
    # remove min element from generated list
    random_list.remove(min(random_list))

print(f"Sorted list: \n{sorted_list}")

# Sub-tasks 3-4
print("\n" + "*" * 20 + " Calculation of average for even and odd numbers" ""
                        "is started " + "*" * 20 + "\n")

# create lists for keeping even and odd numbers
try:
    odd_mb_list = filter(lambda val: val % 2, sorted_list)
    even_nb_list = filter(lambda val: not val % 2, sorted_list)
except ZeroDivisionError:
    pass

# explicitly calculate average and put into appropriate variables
avg_odd_nb = sum(odd_mb_list)/len(odd_mb_list)
avg_even_nb = sum(even_nb_list)/len(even_nb_list)
# display results
print(f"Average for even numbers: {avg_even_nb}. Sum: {sum(even_nb_list)}, "
      f"count: {len(even_nb_list)}")
print(f"Average for odd numbers:  {avg_odd_nb}. Sum: {sum(odd_mb_list)}, "
      f"count: {len(odd_mb_list)}")

print("\n" + "=" * 50 + " Sub-tasks are finished " + "=" * 50 + "\n")
