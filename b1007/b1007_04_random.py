import random

# 1, 25 사이의 랜덤숫자 생성하고 출력
# r_num = random.randint(1, 25+1)

# 1, 25까지 랜덤숫자를 생성, 중복은 제거하고 출력
# a_list = []

# for i in range(25):
#   r_num = random.randint(1, 25+1)
#   if r_num not in a_list:
#     a_list.append(r_num)
# print(a_list)


# 계속 돌려서 1-25까지 다 채우기
# a_list = []
# count = 0
# while len(a_list) < 25:
#   r_num = random.randint(1, 25)
#   if r_num not in a_list:
#     a_list.append(r_num)
#   count += 1
# a_list.sort()
# print(a_list)
# print(f"{count}번 만에 성공")


### random.sample() - 1, 25 랜덤으로 배치 ###
# a_list = []
# for i in range(25):
#   a_list.append(i+1)
# b_list = random.sample(a_list, 25)  # 범위 리스트, 25개 추출(중복 불가)
# print(b_list)

### random.choice() ###
a_list = []
for i in range(25):
  a_list.append(i+1)
b_list = random.choices(a_list, k=25) # 25개 추출, 중복 가능
print(b_list)