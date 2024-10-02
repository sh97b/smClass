# 리스트
# in - 데이터가 있는지 없는지 확인
# count - 데이터 개수
# find - 데이터가 있는 위치를 알려줌, 없으면 -1 반환 (검색어, 시작위치, 끝위치)
# index - 데이터가 있는 위치를 알려줌, 없으면 에러


fruit = "사과, 배, 딸기, 포도, 복숭아, 배, 사과, 배, 딸기"
print("모든 글자 : ", fruit)

# 배가 있는 위치를 모두 출력하시오
search = input("과일 이름을 입력하세요")
idx = 0
if fruit.count(search) > 0:
  print(f"{search} 글자가 있습니다.")
  for i in range(fruit.count(search)):
    print(fruit.find(f"{search} 글자가 있는 위치 : ", idx)) # find(찾을 문자, 시작index, 끝 index)
    idx = fruit.find(search, idx) + 1
else:
  print(f"{search}가 없습니다.")



# 혼자하다가 망함
# pears = 0
# for i in range(pears, len(fruit)):
#   if fruit.find("배"):
#     pears += 1
#     print(f"{pears}")
#     break


# count 문자열 내에 해당 숫자 갯수 확인
# fruit = "사과, 배, 딸기, 포도, 복숭아, 배, 사과, 배, 딸기"
# print(fruit.count("사과"))

# 과일 이름을 입력받아 있으면 있다, 갯수가 몇 개인지 출력
# fruit = "사과, 배, 딸기, 포도, 복숭아, 배, 사과, 배, 딸기"
# i_fruit = input("과일 이름을 입력하시오")
# if i_fruit in fruit:
#   print(f"{i_fruit}가 있습니다.")
#   print("과일 개수 : {}".format(fruit.count(i_fruit)))
#   print(fruit.find(i_fruit))
#   print(fruit.index(i_fruit)) # 과일 위치 index
# else:
#   print(f"{i_fruit}라는 글자가 없음")

# count 리스트에서 갯수 확인
# fruit = ["사과", "배", "딸기", "포도", "복숭아", "배", "사과", "배", "딸기"]
# print(fruit.count("배"))
# print(fruit.count("사과"))


# fruit = ["사과", "배", "딸기", "포도", "배"]

# # 글을 입력받아 입력한 과일이 있으면 있어요 없으면 없어요
# i_fruit = input("과일 이름을 입력하세요")

# if i_fruit in fruit:
#   print(f"{i_fruit}가 있어요")
# else:
#   print("입력한 과일이 없어요")


# fruit = ["사과", "배", "딸기", "포도"]
# if "배" in fruit:
#   print("배라는 글자가 있어요")
# else:
#   print("배라는 글자가 없어요")


# fruit = ["사과", "배", "딸기", "포도", "배"]
# if "배" in fruit: # 한 번의 비교로 있는지 없는지 확인
#   print("배가 있어요")
# else:
#   print("배가 없어요")