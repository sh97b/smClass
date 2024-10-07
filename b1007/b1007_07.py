# a_list = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]
a_list = [
  [0,1,0],
  [0,0,1],
  [1,0,0]
]

while True:
  print("        [ i, j 좌표 ]")
  print("-" * 30)
  print("\t0\t1\t2\t")  # 맨 윗줄
  print("-" * 30)
  for i in range(3):
    print(i,"|",end='\t') # a_list 안에 있는 리스트 개수 0부터시작
    for j in range(3):    # 안에 있는 리스트의 값들
      print(a_list[i][j],end='\t')
    print()
  code = input("좌표를 입력하세요(ex : 0,0) >> ")
  codeArr = code.split(",")   # codeArr[0], codeArr[1]

  a = a_list[int(codeArr[0])][int(codeArr[1])]
  print(f"{codeArr}의 좌표값 : {a}")
  
  if a == 1:
    print("당첨")
  elif a == 0:
    print("꽝")