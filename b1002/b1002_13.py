import random

aArr = []

# 10개의 랜덤숫자(0-9) 추출해서 10번 추가
# 같은 수는 중복 불가하도록 입력

# for문
# for i in range(10):
#   r_num = random.randint(0,9)
#   if r_num not in aArr:
#     aArr.append(r_num)
# print(aArr)

# while문
# while len(aArr) < 10:
#   aArr.append(random.randint(0,9))
# print(aArr)

# 무조건 10개
i = 0
while i < 10: # 10개일 때 종료
  r_num = random.randint(0,9)
  if r_num not in aArr:
    aArr.append(r_num)
    i += 1

print("aArr 개수 : ",len(aArr))
print(aArr)