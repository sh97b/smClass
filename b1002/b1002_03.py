# 100 99 98 A+
# 97 96 95 94 A
# 93 92 91 90 A-
# 89~88 B+
# 87~84 B
# 83~80 B-
# 70점대 C
# 60점 이하 F

# score = int(input("점수를 입력하시오."))

# if 98 <= score <= 100 :
#   print("A+")
# elif 94 <= score :
#   print("A")
# elif 90 <= score :
#   print("A-")
# elif 88 <= score :
#   print("B+")
# elif 84 <= score :
#   print("B")
# elif 80 <= score :
#   print("B-")
# elif 70 <= score :
#   print("C")
# elif 60 <= score < 70 :
#   print("D")
# elif score <= 60 :
#   print("F") 
# else:
#   print("점수를 잘못 입력하셨습니다.")

num = int(input("숫자를 입력하시오"))
score = ""

if 90 <= num :
  score = "A"
  if 98 <= num:
    score += "+"
elif 80 <= num :
  score = "B"








# # 입력한 숫자가 1보다 크거나 같고 10보다 작거나 같을 때만 정답입니다. 그렇지 않으면 오답입니다.
# num = int(input("숫자를 입력하시오"))

# if num >= 1 and num <= 10 :   # if 1 <= num <= 10 :
#   print("정답입니다.")         # print("정답입니다.")
# else :
#   print("오답입니다.")


# # 입력한 숫자가 10보다 작고같거나 100보다 크거나 같을 떄 정답, 아니면오답입니다.

# a = int(input("숫자를 입력하시오"))

# if a <= 10 or num >= 100:
#   print("정답입니다.")
# else :
#   print("오답입니다.")


# 숫자를 입력받아
# 345봄 678여름 91011가을 1212겨울
# season = int(input("숫자를 입력하시오"))

# if 3 <= season <= 5 :
#   print("봄입니다.")
# elif 6 <= season <= 8 :
#   print("여름입니다.")
# elif 9 <= season <= 11 :
#   print("가을입니다.")
# elif 1 <= season <= 2 or season == 12 :
#   print("겨울입니다.")
# else :
#   print("숫자를 다시 입력하세요.") 


# # 입력한 숫자가 짝수인지 홀수인지 출력
# a = int(input("숫자를 입력하시오"))

# if a % 2 == 0 :
#   print("짝수입니다.")
# else :
#   print("홀수입니다.")