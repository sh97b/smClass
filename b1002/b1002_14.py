import random

# 숫자 스무고개같은 게임
# 1-100까지의 랜덤숫자
# 입력한 숫자가 랜덤숫자보다 크면 입력한 숫자가 큽니다.
# 입력한 숫자가 랜덤숫자보다 작으면 입력한 숫자가 작습니다.
# 10번 도전해서 맞히기
# 정답입니다. 프로그램 종료하십시오 break
# for, while 둘 다 

# while
# r_num = 0
# count = 0

# numbers = random.randint(1,100)

# while count < 10:
#   search = int(input("숫자를 입력하세요"))
#   for s in numbers:
#     if s == search:
#       print("정답입니다.")
#       break
#     elif s > search:
#       print("입력한 수가 랜덤숫자보다 큽니다.")  
#     elif s < search:
#       print("입력한 수가 랜덤숫자보다 작습니다.")


### while ###
# count = 0
# i = 0  # 초기값
# r_num = random.randint(1,100) # 랜덤숫자는 while 밖에 있어야 함. 안에 있으면 돌떄마다 숫자 변경됨
# while i < 10: # 조건식
#   input_num = int(input("숫자를 입력하시오")) # str -> int변경, 10번 받아야 하니까 while안에 넣음

#   if r_num < input_num:
#     print("입력한 숫자가 큽니다.")
#   elif r_num > input_num:
#     print("입력한 숫자가 작습니다.")
#   else:
#     print("정답입니다. 정답번호 : ", input_num)
#     count = 1
#     break
#   i += 1  # 증감식

# # 10번 도전에서 실패할 경우
# if count == 0:
#   print("10번 도전에 실패하셨습니다. 정답번호 : ", r_num)


### for ###
r_num = random.randint(1,100)
count = 0
for i in range(10):
  input_num = int(input("숫자를 입력하시오"))
  if r_num < input_num:
    print("숫자가 큽니다.")
  elif r_num > input_num:
    print("숫자가 작습니다.")
  else:
    print("정답입니다.")
    count = 1
    break
  i += 1
if count == 0:
  print("도전 실패")