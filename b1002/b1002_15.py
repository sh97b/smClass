# 숫자맞추기
import random

r_num = random.randint(1,100)
i = 0
count = 0

while i < 10:
  i_num = int(input("숫자를 입력하시오"))
  if i_num > r_num:
    print(f"입력한 수가 더 큽니다. {i+1}번쨰 도전입니다.")
  elif i_num < r_num:
    print(f"입력한 수가 더 작습니다. {i+1}번쨰 도전입니다.")
  else:
    print(f"정답입니다. {i+1}번째만에 성공")
    count = 1
    break
  i += 1
if count == 0:
  print("도전 실패")