# # 문자열
# # 문자열 숫자
# a = "123"
# print(type(a))
# print(type(int(a)))
# print(type(float(a)))

# b = 12.3
# # print(type(int(b))) # 애러 - 소숫점이 잇는 문자열 숫자는 float변경해야 함
# print(type(float(b)))

# c = 12.3
# print(type(int(c))) # 실수는 int 타입으로 변경이 가능함
# print(int(c)) # 결과 : 12

# s1 = "안녕"
# s2 = "안녕하세요"
# print(s1 + s2)
# # print(a + b)  # 문자열연결연산자
# # print(a * b)  # 에러 - 문자열은 -, *, / 안됨

# # 문자열반복연산자
# print("안녕 " * 10)
# print("--" * 30)

# 문자열 슬라이싱
str1 = "안녕하세요.반갑습니다." # 문자열 자체 - 리스트
print(str1[0])  # 해당번호 넣으면 해당되는 문자 출력
print(str1[6])
print(str1[2:5])  # [여기부터:여기 앞전까지] 해당 범위 출력
print(str1[:5])  # [처음부터 여기 앞까지]
print(str1[2:])  # [여기부터:끝까지]
print(str1[1:10:2])  # [여기부터:여기 앞까지:2칸씩]
print(str1[1:10:3])  # [여기부터:여기 앞까지:3칸씩]
print(str1[::-1])    # 거꾸로(역순)

# [] - 배열 : 한번 범위가 정해지면 수 정 불가 : c, 자바
# [] - 리스트 : 범위 상관 없음



# input_str = input("글자를 입력하세요")

# # 문자가 입력되지 않았을 때 if문
# if input_str != "": # 빈공백이 아니냐
#   print("입력문자 : ", input_str)
#   print("프로그램이 종료됩니다.")
# else:
#   print("글자를 입력하셔야 합니다.")
