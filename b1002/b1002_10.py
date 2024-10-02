fruit = []

# 입력된 과일이름을 리스트에 추가하시오
while True:
  # strip() - 앞뒤여백제거(trim같은것) ' 사과'->'사과'/ '사과  '->'사과'
  # '사 과' <이렇게 사이공백은 replace쓰면 됨
  # replace(" ", "") : 문자 대체 함수
  search = input("과일이름을 입력하시오. (종료: x) ").replace(" ","")
  # search = input("과일이름을 입력하시오. 종료: x").strip()
  if search == 'x':
    print("프로그램을 종료합니다.")
    break
  if(search in fruit):
    print("같은 과일이 이미 있습니다.")
  else:
    print(f"{search}를 추가합니다.")
    fruit.append(search)
    print(fruit)


# break - 반복문을 종료할 떄
# while True:
#   break

# print("프로그램 종료")


# 무한 반복문 while True
# a = 0
# while True: # 무한루프
#   print(a)
#   a += 1


# while a < 10:
#   a += 1
#   print(a)

# print("프로그램 종료")