### list에 데이터 추가하는 법 ###
# append - 맨 뒤에 추가, insert - 원하는 위치에 추가

a_list = [1, 2, 3]
print(a_list) # [1, 2, 3]

a_list.append(4)
print(a_list) # [1, 2, 3, 4]

a_list.append(10)
print(a_list) # [1, 2, 3, 4, 10]

a_list.insert(0,50)
print(a_list) # [50, 1, 2, 3, 4, 10]

a_list.insert(3, 20)
print(a_list) # [50, 1, 2, 20, 3, 4, 10]


### list에 있는 데이터 삭제하는 법 ###
# del - index 위치에 있는 데이터 삭제, remove - 데이터값 삭제
del a_list[0]
print(a_list) # [1, 2, 20, 3, 4, 10]  0번째에 있던 50이 삭제됨

del a_list[2]
print(a_list)  # [1, 2, 3, 4, 10] 2번째에 있던  20이 삭제됨

a_list.remove(4)
print(a_list)  # [1, 2, 3, 10] 4가 삭제됨

a_list.remove(10)
print(a_list)  # [1, 2, 3] 10이 삭제됨



stu = [1, "홍길동", 100, 100, 100, 99]
# 합계, 평균 추가
total = stu[2]+stu[3]+stu[4]+stu[5]
stu.append(total)
stu.append(total/4)
print(stu)