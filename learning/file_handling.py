
### Manualy open/close a file.

# file = open("text.txt")
# file.seek(10)
# print(file.tell())

# ### using A Context manager
# with open("text.txt", "r") as f:
#         line_by_line = f.readlines() # creates a list where each line is an item


# print(line_by_line[0])

my_list = ["router eigrp 1", "router-id 1.1.1.1", "network 0.0.0.0"]
with open("text.txt", "w") as f:
    f.writelines(my_list)
