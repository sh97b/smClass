import random

# 1-25까지 랜덤숫자 25개 중복없이 추출해서
# 5*5 2차원 배열에 넣기
a_list = []
for i in range(25):
  a_list.append(i + 1)
print(a_list)

random.shuffle(a_list)
print(a_list)

# 0부터 a_list길이까지 5씩 증가
b_list = []
for i in range(0, len(a_list), 5):
  b_list.append(a_list[i:i+5])

# b_list에는 1-25를 랜덤으로 섞어서 5*5의 이차원 리스트가 있음
while True:
  print("\t0\t1\t2\t3\t4\t")
  print("-" * 50)
  for i in range(5):
    print(i, end='\t')
    for j in range(5):
      print(b_list[i][j], end='\t')
    print()
  i_xy = input("좌표를 입력하세요. (0,1) >> ")
  i_xy2 = i_xy.split(",")
  print(i_xy2)
  print(f"{i_xy}좌표의 값 : {b_list[int(i_xy2[0])][int(i_xy2[1])]}")

# ### 랜덤숫자 받아오기 ###
# a_list = []
# for i in range(25):
#   a_list.append(i+1)
# b_list = random.sample(a_list, 25)
# b_list.sort()
# print(b_list)

# ### 이차원배열로 변경 ###
# c_list = []
# for i in range(5):
#   a = []
#   for j in range(5):
#     a.append(a_list[i * 5 + j])
#   c_list.append(a)
# print(c_list)