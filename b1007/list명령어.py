# 리스트
# 배열 - 같은 타입만 묶을 수 있음, 크기 수정 불가
# 리스트 - 다른 타입 o, 크기 수정 o

### 리스트 함수 ###
a_list = [1, 2, 3, 4, 3, 5, 60, 3, 70, 3]
# 리스트 함수 - 추가
# a_list.append(200)    # 맨 뒤에 값 추가

# 리스트 함수 - 삭제
# a_list.pop(2)     # 해당 인덱스의 위치 삭제
# a_list.remove(3)  # 리스트 안에 있는 5라는 값을 삭제
# del(a_list[3])    # [1, 2, 3, 3, 5, 60, 3, 70, 3] - 해당 위치 값 삭제
# a_list.clear()    # 전체 삭제

# print(len(a_list))    # 리스트 길이
# print(f"{a_list.count(3)}개")  # 입력된 값의 존재 개수. 3은 4개 있음
# a_list.insert(0, 100) # 인덱스 위치에 해당 값 저장 (0번째 위치에, 100이라는 값 저장)
print(a_list)



### 리스트 삭제 ###
# a_list = [1, 2, 3, 4, 5]

# a_list[1:3] = [] # [2, 5] - 2개 삭제 [n부터:m전까지]삭제
# a_list = []      # 전체 삭제
# a_list = None    # 전체 삭제
# del(a_list)      # 리스트 자체를 삭제

# print(a_list)

# del 명령어 사용 #
# del a_list[0]    # [2, 3, 4, 5] - 0번째 리스트 삭제
# print(a_list)


### 리스트 수정 방법 ###
# a_list = [1, 2, 3, 4, 5, 6, 7]
# a_list[3] = 50          # 1개 변경 시
# a_list[1:2] = [20, 30]  # 2개 변경 시
# a_list[4] = [10, 20]    # 리스트 안에 리스트로 변경(이차원리스트) [1, 20, 30, 3, [10, 20], 5, 6, 7]
# print(a_list)


### 리스트 출력 방법 ###
# a_list = [1, 2, 3, 4, 5]
# b_list = [50, 100]

# print(a_list[3])        # 4
# print(a_list[0:3])      # [1, 2, 3]
# print(a_list[2:4])      # [3, 4]
# print(a_list[:3])       # [1, 2, 3]
# print(a_list[3:])       # [4, 5]
# print(a_list + b_list)  # [1, 2, 3, 4, 5, 50, 100]
# print(b_list * 3)       # [50, 100, 50, 100, 50, 100]
# print(a_list[::2])      # [1, 3, 5] 2씩 뛰어서
# print(a_list[::-2])     # [5, 3, 1] 거꾸로 2씩 뛰어서
# print(a_list[::-1])     # [5, 4, 3, 2, 1] 거꾸로
# print(a_list[:])        # [1, 2, 3, 4, 5]
# print(a_list)           # [1, 2, 3, 4, 5]


### 깊은복사 - 리스트를 역순으로 저장 ###
# a_list = [1,2,3,4,5]
# b_list = a_list[::-1] # 이렇게 거꾸로 하면 
# print(a_list)         # a_list와 b_list가 같은 공간에 있는 게 아니고 
# print(b_list)         # 새로운 게 각각 생겨서
# a_list[0] = 100       # a_list를 수정하면
# print(a_list)         # a_list의 값만 수정되고
# print(b_list)         # b_list의 값 변하지 x

### 얕은복사 / 깊은복사 ###
# a_list = [1,2,3,4,5]
# b_list = a_list   # 얕은복사
# a_list[0] = 100   # a_list의 값 변경하면 b_list의 값도 변경됨
# print(a_list)
# print(b_list)   

# a_list = [1,2,3,4,5]
# b_list = a_list[:]   # 깊은복사
# a_list[0] = 100      # a_list의 값 변경해도 b_list의 값 변경되지 XX
# print(a_list)
# print(b_list)


# a_list = [1, 2, 3, 4, 5]
# # for i in a_list:
# #   print(i)

# # 역순 출력
# # 리스트 길이만큼 돌음
# for i in range(5):
#   print(a_list[-(i+1)]) # i = 0,1,2,3,4   # 맨 마지막은 -1
#                         # -(0+1), -(1+1), -(2+1), -(3+1), -(4+1)
# # for i in range(len(a_list)):
# #   print(a_list[-(i+1)])


# # 숫자(정수형), 숫자(실수형), 문자열, 논리형
# a_list = [1, 2, 3.0, "안녕", True, False]
# print(a_list[0])
# print(a_list[3])
# print(a_list[-1])
# print(a_list[::-1])


# a_list = []
# total = 0
# # 1-100 들어가 있는 리스트 출력
# for i in range(100):
#   i += 1
#   a_list.append(i)
#   total += i + 1
# print(a_list,f"\n합계 : {total}")


### 빈 리스트 ###
# a_list = []
# total = 0

# for i in range(7):
#   j = int(input(f"{i+1}번쨰 숫자 입력 : "))
#   a_list.append(j)
#   total += j
# print("합계 :", total)


### 인덱스값 ###
# a_list = [0, 0, 0, 0, 0, 0, 0]
# total = 0

# for idx, a in enumerate(a_list):
#   a = int(input(f"{idx+1}번째 숫자 입력 : "))
#   total += a
# print("합계 :", total)


### 변수 ###
# a, b, c, d, e, f, g = 0, 0, 0, 0, 0, 0, 0
# total = 0

# # 변수 a,b,c,d,e에 숫자를 입력받아 합계 출력
# a = int(input("첫 번째 숫자 입력 : "))
# b = int(input("두 번째 숫자 입력 : "))
# c = int(input("세 번째 숫자 입력 : "))
# d = int(input("네 번째 숫자 입력 : "))
# e = int(input("다섯 번째 숫자 입력 : "))
# f = int(input("여섯 번째 숫자 입력 : "))
# g = int(input("일곱 번째 숫자 입력 : "))

# total = a + b + c + d + e + f + g
# print("합계 : ", total)