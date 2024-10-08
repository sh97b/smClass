### 좌표 ###

# [0,3,6,9,12...]
# aArr = []
# for i in range(20):
#   aArr.append(3 * i)
# # print(aArr)

# # 4 * 5 이차원리스트
# a_list = []
# for i in range(4):
#   a = []
#   for j in range(5):
#     a.append(aArr[5 * i + j])
#   a_list.append(a)
# print(a_list)



# # 4 * 5 이차원리스트
a_list = []

for i in range(5):
  l = []
  for j in range(5):
    # l.append((i * 5) + j + 1)
    l.append(5 * 3 * i + (j * 3))
  a_list.append(l)

for i in range(4):
  for j in range(5):
    print(a_list[i][j],end='\t')
  print()