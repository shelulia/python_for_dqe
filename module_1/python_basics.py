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
random_list = [random.randrange(0, 1000) for st in range(100)]

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
odd_mb_list = list(filter(lambda val: val % 2, sorted_list))
even_nb_list = list(filter(lambda val: not val % 2, sorted_list))


# explicitly calculate average and put into appropriate variables
try:
    avg_odd_nb = (sum(odd_mb_list)/len(odd_mb_list) if odd_mb_list else [])
    avg_even_nb = (sum(even_nb_list)/len(even_nb_list) if even_nb_list else [])
except ZeroDivisionError as e:
    pass

# display results
print("There are no even numbers in generated list" if not avg_even_nb else
      f"Average for even numbers: {avg_even_nb}. Sum: {sum(even_nb_list)}, "
      f"count: {len(even_nb_list)}" )
print("There are no odd numbers in generated list"  if not avg_odd_nb else
      f"Average for odd numbers:  {avg_odd_nb}. Sum: {sum(odd_mb_list)}, "
      f"count: {len(odd_mb_list)}")

print("\n" + "=" * 50 + " Sub-tasks are finished " + "=" * 50 + "\n")
