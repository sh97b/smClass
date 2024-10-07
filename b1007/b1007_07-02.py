import random

lotto = [0] * 6 + [1] * 3
random.shuffle(lotto)

a_list = [
  [0,1,0],
  [0,0,1],
  [1,0,0]
]

for i in range(3):
  for j in range(3):
    a_list[lotto[(i * 3) + j]]


aa_list = [
  ['로또','로또','로또'],
  ['로또','로또','로또'],
  ['로또','로또','로또']
]


while True:
  myMoney = int(input("얼마를 투자하시겠씁니까? >> "))


  print("        [ i, j 좌표 ]")
  print("-" * 30)
  print("\t0\t1\t2\t")  # 맨 윗줄
  print("-" * 30)
  for i in range(3):
    print(i,"|",end='\t') # a_list 안에 있는 리스트 개수 0부터시작
    for j in range(3):    # 안에 있는 리스트의 값들
      print(aa_list[i][j],end='\t')
    print()
  code = input("좌표를 입력하세요(ex : 0,0) >> ")
  codeArr = code.split(",")   # codeArr[0], codeArr[1]

  a = aa_list[int(codeArr[0])][int(codeArr[1])]
  print(f"{codeArr}의 좌표값 : {a}")
  
  if a == 1:
    a = "당첨"
    print(f"{codeArr} : 당첨")
    print(f"{codeArr} 당첨금 : {myMoney * 10:,d}")
  elif a == 0:
    a = "꽝"
    print(f"{codeArr} : 꽝")
    print(f"{codeArr} 다음 기회에 : {myMoney * 10:,d}")