# 2차원 리스트
# for문을 중첩사용해서 1부터 25까지 5*5 리스트 생성하기
a_list = []
for i in range(5):
  a = []
  for j in range(5):
    a.append((i * 5) + (j + 1))
  a_list.append(a)
print(a_list)


# a_list = []   #a_list[0], a_list[1], ... , a_list[8]
# for i in range(9):
#   a_list.append(i+1)
# print(a_list)

# b_list = []
# for i in range(9):
#   b = []
#   if(a_list[i] % 4) == 0:
#     b.append



# [3, 3] 리스트 [1, 2, 3], [4, 5, 6], [7, 8, 9]

# 1-9 2차원 리스트에 추가
# a_list = []
# for i in range(0, 3):
#   a = []
#   for j in range(0, 3):
#     a.append((i*3)+(j+1))
#   a_list.append(a)
# print(a_list)

# 1-9 리스트 추가
# b_list = []
# for i in range(1, 9+1):
#   b_list.append(i)
# print(b_list)



# 다차원 리스트
# a_list = [
#   [1, 2, 3, 4],
#   [5, 6, 8],
#   [9, 11, 12]
# ]

# 2차원 리스트
# a_list = [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9, 10, 11, 12]
# ]
# # 2차원 리스트는 for문을 중첩해서 써야 함
# for i in a_list:
#   for j in i:
#     print(j)