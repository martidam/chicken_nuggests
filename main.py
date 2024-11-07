color_list = ["red", "green", "blue", "yellow"]
print("first element:", color_list[0])
print("last element:", color_list[-1])
slice_list = color_list[1:3]
print("slice list (second and third elements):", slice_list)
num_list = [4, 6, 4, 2, 9, 4, 1]
num_list.append(5)
print("updated num_list after appending 5:", num_list)
num_list.remove(4)
print("updated num_list after removing first occurrence of 4:", num_list)
count_of_4 = num_list.count(4)
index_of_9 = num_list.index(9)
print("index of the first occurrence of 9 in num list:", index_of_9)
fruit_list = ["apple", "banana", "cherry"]
fruit_list[1] = "orange"
fruit_list.pop()


