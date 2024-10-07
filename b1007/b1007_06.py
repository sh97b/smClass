import random

# 숫자 25개가 들어있는 일차원 리스트
# 25개 중 1을 5개, 나머지는 0으로 입력해서 출력
a_list = ([0]*20) + ([1] * 5)
random.shuffle(a_list)

# 2차원 리스트(이름: b_list)에 a_list의 값을 5 * 5로 넣고 출력
b_list = []
for i in range(5):
  a = []
  for j in range(5):
    a.append(a_list[i * 5 + j])  # a에 a_list[0], a_list[6], a_list[12], a_list[18], a_list[24]를 추가
  b_list.append(a)  # b_list에 a를 추가
print(b_list)

# 5*5
while True:
  print("\t0\t1\t2\t3\t4\t")
  print("-" * 40)
  for i in range(5):
    print(i, end='\t')
    for j in range(5):
      print(b_list[i][j], end='\t')
    print()

  num = input("좌표를 입력하세요(ex : 0,0) >> ")
  num2 = num.split(",")
  print(num2)
  print(f"{num}좌표값 : {b_list[int(num2[0])][int(num2[1])]}")


# 혼자 하다 망함 shit
# while True:
#   print("\t0\t1\t2\t3\t4\t")
#   print("-" * 40)

#   b_list = []
#   for i in range(5):
#     print(i, end='\t')
#     a = []
#     for j in range(5):
#       a.append(a_list[i * 5 + j])
#       print(a[i][j], end='\t')
#     print()
#     b_list.append(a)
#   print(b_list)



# a_list = []
# for i in range(25):
#   if i < 5:
#     a_list.append(1)
#   else:
#     a_list.append(0)
# print(a_list)