import random

print("=" * 50 + " Module 1 " + "=" * 50 + "\n")
#Sub-task 1
print("*" * 20 + " Creation of list of 100 random numbers from 0 to 1000 is started " + "*" * 20 + "\n")
#Create empty list to put random numbers there
random_list = []
#declare step
st = 0
#start loop for puttinh random numbers
while st < 100:
    #append random numbers to the list
    random_list.append(random.randrange(0, 1000))
    #iterate
    st += 1

print(f"List of random numbers was created: \n{random_list}")

#Sub-task 2
print("\n" + "*" * 20 + " Sorting the list of random numbers is started " + "*" * 20 + "\n")

#for all 100 elements
for i in range(len(random_list)):
    #for elements from 1 till 100 (excleding 0 element)
    for j in range(i + 1, len(random_list)):
        #Compare if 1 elem is greater than next one
        if random_list[i] > random_list[j]:
            #Put it into correct place (change place)
            random_list[i], random_list[j] = random_list[j], random_list[i]

print(f"Sorted list: \n{random_list}")

#Sub-tasks 3-4
print("\n" + "*" * 20 + " Calculation of average for even and odd numbers is started " + "*" * 20 + "\n")

#declare empty lists for keeping even and odd numbers
even_nb_list = []
odd_mb_list = []

#start checks for each element in list
for elem in random_list:
    #validate if element has left part after dividing - then odd, else - even. Append elements to appropriate lists
    if elem % 2:
        odd_mb_list.append(elem)
    else:
        even_nb_list.append(elem)
#explicitly calculate average and put into appropriate variables
avg_odd_nb = sum(odd_mb_list)/len(odd_mb_list)
avg_even_nb = sum(even_nb_list)/len(even_nb_list)
#display results
print(f"Average for even numbers: {avg_even_nb}. Sum: {sum(even_nb_list)}, count: {len(even_nb_list)}")
print(f"Average for odd numbers:  {avg_odd_nb}. Sum: {sum(odd_mb_list)}, count: {len(odd_mb_list)}")

print("\n" + "=" * 50 + " Sub-tasks are finished " + "=" * 50 + "\n")
