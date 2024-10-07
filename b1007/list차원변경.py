# 1차원 리스트 : 1-25
a_list = []
for i in range(25):
  a_list.append(i+1)
print(a_list)

b_list = []
# (0에서, 25까지, 5씩 증가)
for i in range(0, len(a_list), 5):
  b_list.append(a_list[i:i+5])  # [0:5] [5:10] [10:15]...
print(b_list)





# 1차원 리스트 -> 2차원 리스트 변경
# b_list = []
# for i in range(5):
#   b = []
#   for j in range(5):
#     b.append((i * 5) + (j + 1))
#   b_list.append(b)
# print(b_list)


# a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b_list = []

# for i in range(3):
#   list = []
#   for j in range(3):
#     list.append((i * 3) + (j + 1))
#   b_list.append(list)
# print(b_list)
