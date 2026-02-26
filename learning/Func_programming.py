# task 1 create a new lists the contains all items in the my_list_of_interfaces list
#  if they start with "Gig"
my_list_of_interfaces = ["Gig0/0", "Fa0/0", "Gig0/1", "Gig0/2", "Loopback0", "Port-Channel1"]


# #option 1 use list comprehension

# new_list = [i for i in my_list_of_interfaces if i.startswith("Gig")]
# print(new_list)

# #option 2 use lambda and filter

# filter_func = lambda x: x.startswith("Gig")
# new_list = list(filter(filter_func, my_list_of_interfaces))
#-------------------------------------------------------------------------------------



# task 2 calculate the sum of all items in my_list_of_nums and print as string.
my_list_of_nums = [0,1,2,3,4,5]

# #option 1 use the reduce function
# from functools import reduce
# adder = lambda x,y: x+y

# answer = reduce(adder, my_list_of_nums)
# print(answer)

# #option 2 use for loop
# total=0 
# for i in my_list_of_nums: 
#     total+=i
# print(total)

# #option 3 use built-in function
# total = sum(my_list_of_nums)
# print(total)
