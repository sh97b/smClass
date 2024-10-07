import random

lotto = [0] * 6 + [1] * 3
random.shuffle(lotto)

a_list = [
  [0,1,0],
  [0,0,1],
  [1,0,0]
]

# i : 행  [], [], []
# j : 열  0,1,0
for i in range(3):
  for j in range(3):
    a_list[i] = lotto[(i * 3) + j]  # a_list의 값을 shuffle한 lotto의 값으로 변경


aa_list = [
  ['로또','로또','로또'],
  ['로또','로또','로또'],
  ['로또','로또','로또']
]

while True:
  myMoney = int(input("얼마를 투자하시겠습니까? >> "))

  print("        [ i, j 좌표 ]")
  print("-" * 30)
  print("\t0\t1\t2")  # 맨윗줄
  print("-" * 30)
  
  for i in range(3):
    print(i, "|", end='\t')
    for j in range(3):
      print(aa_list[i][j],end='\t')
    print()
  
  code = input("좌표를 입력하세요(예시 : 0,0) >> ")
  codeArr = code.split(",")

  a = aa_list[int(codeArr[0])][int(codeArr[1])]
  print(f"{codeArr}의 좌표값 : {a}")

  if a == 1:
    print(f"{codeArr} : 당첨")
  elif a == 0:
    print(f"꽝")