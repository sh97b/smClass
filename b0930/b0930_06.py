# 학생이름 : 홍길동
# 국어 : 100
# 영어 : 100
# 수학 : 100
# 과학 : 99
# 합계 : 
# 평균 : 

stu_data = ["홍길동", 100, 100, 100, 99]
# for s in stu_data:
#   print(s)

stu_title = ['번호', '이름', '국어', '영어', '수학', '과학', '합계', '평균']
stu_datas = [
 [1, "유관순", 100, 100, 100, 99],
 [2, "이순신", 100, 99, 98, 99],
 [3, "김구", 80, 100, 90, 99]
]

# 

print("                     [학생성적프로그램]")

for s_t in stu_title:
  print("{}".format(s_t), end='\t') # end='' <이거 안 쓰면 원래 기본값이 end='\n' : 줄바꿈
print() # 줄바꿈 == \n
print("-" * 62)

for s in stu_datas:
  total = s[2] + s[3] + s[4] + s[5]
  avg = total / 4
  print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(s[0], s[1], s[2], s[3], s[4], s[5], total, avg))
print("-" * 62)

# print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(stu_title[0], stu_title[1], stu_title[2], stu_title[3], stu_title[4], stu_title[5], stu_title[6], stu_title[7]))
# print("-" * 60)


# 내맘대로
# for s in stu_datas:
#   total = s[2] + s[3] + s[4] + s[5]
#   avg = total/4
#   print(s[1], s[2], s[3], s[4], "합계 : {}, 평균 : {}".format(total, avg))


# 이순신의 평균을 출력하시오
# lee_avg = (stu_datas[1][1] + stu_datas[1][2] + stu_datas[1][3] + stu_datas[1][4]) / 4
# print(lee_avg)


# total = stu_data[1] + stu_data[2] + stu_data[3] + stu_data[4]
# avg = total / 4

# print("학생이름 : %s" % stu_data[0])
# print("국어 : {}".format(stu_data[1]))
# print(f"영어 : {stu_data[2]}")
# print("수학 : {}".format(stu_data[3]))
# print("과학 : {}".format(stu_data[4]))
# print(f"합계 : {total}")
# print(f"평균 : {avg:.2f}")


# 한 번에 두 개 길이를 입력받아 삼각형의 넓이와 사각형의 넓이 구하기
# length = input("두 개의 길이를 입력하세요")
# print(length.split(" "))

# l_list = length.split(" ")
# print("삼각형의 넓이 : {}".format((float(l_list[0]) * float(l_list[1]))/2))
# print("사각형의 넓이 : {}".format((float(l_list[0]) * float(l_list[1]))))


# 두 개의 길이를 입력받아 삼각형의 넓이와 사각형의 넓이 구하기
# n = int(input("가로 길이를 입력하시오"))
# m = int(input("세로 길이를 입력하시오"))
# tri = (n * m)/2
# square = n * m
# print("삼각형의 넓이 : {}, 사각형의 넓이 : {}".format(tri, square))

# 원의 넓이 : 반지름 ** 2 * 3.14
# 반지름을 입력받아 원의 넓이 구하기

# r = float(input("반지름의 길이를 입력하시오"))
# area = r ** r * 3.14
# print("원의 넓이 : {:.2f}".format(area))


### 복합대입연산자 ###
# +=, -=, *=, /=, %=, //=, **=
# a = 10
# a += 5; print(a)
# a -= 5; print(a)
# a *= 5; print(a)
# a /= 5; print(a)
# a //= 5; print(a)
# a **= 5; print(a)
# a %= 5; print(a)


# 파이썬에는 i++ (증감연산자), switch문 없음.if문 써야 함


### 숫자를 문자열로 변환 ###
# 문자열 + 숫자 <불가능
# a = 100
# b = 10
# print(str(a) + str(b))


### 문자형 숫자 변환 ###
# a = "100"
# b = "10.5"
# c = "안녕"
# print(float(a)) # 정수형 -> 정수타입, 실수타입 변경 가능
# # print(int(b)) # 실수형 -> 정수타입 변경 불가, 실수타입 변경 가능
# # print(float(c))  # 문자는 숫자타입으로 변경 불가
# int("안녕")  # 이렇게 쓸 수 없음


# a = 10
# b = 5

# 변수 한줄로 선언하는 방법 1
# a = 10; b = 5
# 변수 한 줄로 선언하는 방법 2
# s1, s2, s3 = 1, 2, 3 


### 이것의 정체 알아내기 ###
# x = 1, 2, 3, 4, ... 10
# 1
# x = 11, 12, 13 ... 20
# 11
# x = 21, 22, 23 ... 30
# 21


# 0, 1, 3, 5, 7, 9
# 2x + 1


# 우선순위
# print(2 + 2 - 2 * 2 / 2 * 2)


# a = 5; b = 3  # 한 줄로 적으려면 ; 넣으면 ㅗ딤
# a = 5
# b = 3

# print("{:.2f}, {}, {}, {}".format(a/b, a%b, a//b, a**b))