fruit = "사과,배,딸기,포도,복숭아,배,사과,배,딸기"

fruits = fruit.split(",")
# print(fruits)
# print(len(fruits))

# 리스트인 경우 해당되는 인덱스를 출력하시오
# 배에 해당되는 인덱스 번호를 출력

search = input("검색하려는 과일을 입력")
for idx, f in enumerate(fruits):
  if f == search :
    print("해당 위치 : " ,idx)



  



# print(fruit.find("배", 0))  # 3
# print(fruit.find("배", 3+1))
# print(fruit.find("배", fruit.find("배", 0)+1))  # 15
# print(fruit.find("배", 15+1))
# print(fruit.find("배", fruit.find("배", fruit.find("배", 0)+1)+1))  # 20


# print(fruit.find("딸기", 0))
# print(fruit.find("딸기", fruit.find("딸기", 0)+1))
# print(fruit.find("딸기", 6))