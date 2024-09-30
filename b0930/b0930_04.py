# 타입 - str, float, int, bool  
# 웹에서 (ex)input) 받는 모든 값은 문자형. 타입 변환이 중요함

# name, kor, eng, math, total, avg
# input으로 입력받아서 
# 홍길동, 100, 100, 99, 합계, 평균 한 줄로 출력
# format, f함수 사용
name = input("이름을 입력하시오 : ")
kor = int(input("국어 점수를 입력하시오 : ")) # str에서 int로 타입 변경
eng = int(input("영어 점수를 입력하시오 : "))
math = int(input("수학 점수를 입력하시오 : "))
total = kor + eng + math
avg = total / 3

print("{}, {}, {}, {}, {}, {:.2f}".format(name, kor, eng, math, total, avg))  # format
print(f"{name}, {kor}, {eng}, {math}, {total}, {avg:.2f}")  # f함수



# a = '100'
# b = "200"
# print(type(a))
# print(type(b))

# print(a+b)  # 문자연결연산자 100200
# print(int(a) + int(b)) # 타입 변경

# name = "홍길동"
# # print(int(name))  # 문자를 숫자로 변경 불가. 숫자를 문자로 변경하는 것은 가능

# c = "3.14"
# print(int(float(c)))  # float로 변경 후 int로 변경해야 가능. 
# # print(int(c)) # int로 바로 변경하면 에러남
# print(str(c)) # float를 str로 변경하는 것은 가능

# d = "True"
# print(bool(d))  # 문자 bool형을 bool형으로 변경


# name = "홍길동"
# print(type(name))
# level = '3레벨'
# print(type(level))

# n = 3.14
# print(type(n))

# num = 100
# print(type(num))

# a_bool = True # True, False는 첫글자를 대문자로 넣어야 함
# print(type(a_bool))



# var1 = 100
# var2 = var1
# var3 = var2
# var4 = var3

# print(var4)

# v4 = v3 = v2 = v1 = 10
# print(v4)