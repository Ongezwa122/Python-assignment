### Creating a list and Modifying it ###
### Question 1 creating an empty list
my_list = []

### Question 2 Append list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print("After appending:", my_list)

### Question 3 Insert
my_list = [10,20,30,40]
my_list.insert(1,15)
print("After inserting:", my_list)

### Question 4 
my_list.extend([50,60,70])
print("After extending:",my_list)

### Question 5 Popping
my_list.pop(7)
print("After popping:", my_list)

### Question 6 
my_list.sort() ### Sorting in Ascending order
print("After sorting:",my_list)

### Question 7  Printing an index of a Value
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
