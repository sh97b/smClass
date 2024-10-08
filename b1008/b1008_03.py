# 값이 25개 들어있는 1차원 리스트 (1, 25) 랜덤으로 출력
# 5*5 이차원 리스트 출력
import random

aArr = []
for i in range(25):
  aArr.append(i + 1)

random.shuffle(aArr)



a_list = []
for i in range(5):
  a = []
  for j in range(5):
    a.append(aArr[5 * i + j])
  a_list.append(a)



### 5*5 리스트 출력###
while True:
  print("  |\t0\t1\t2\t3\t4\t")
  print("-" * 60)
  for i in range(5):
    print(i,'|',end='\t')
    for j in range(5):
      print(a_list[i][j], end='\t')
    print()
  
  # ### 좌표 입력하면 값 출력 ###
  # i_xy = input("좌표를 입력하세요(ex: 0,0) >> ")
  # result = i_xy.split(",")
  # print("현재 좌표 : {}".format(a_list[int(result[0])][int(result[1])]))

  ### 값 입력하면 좌표 출력 ###
  result = int(input("값 입력(1-25) >> "))
  if 0 > result > 25:
    print("1에서 25 사이의 값을 다시 입력하세요.")
    continue
  for i in range(5):
    for j in range(5):
      if a_list[i][j] == result:
        print(f"좌표값 : [{i,j}]")
        a_list[i][j] = 0
        break
        

  # 혼자하다 망함
  # result = input("값 입력 >> ")
  # i_xy = a_list[int(result[0])][int(result[1])]
  # for i in range(5):
  #   for j in range(5):
  #     if result == i_xy