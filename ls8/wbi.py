# Given the following array of values, print out all the elements in reverse order, with each element on a new line.
# For example, given the list
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# Your output should be
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

x = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

for i in range(len(x)):
    print(x[-1-i])

# OR

# for i in x[::-1]:
#     print(i)
