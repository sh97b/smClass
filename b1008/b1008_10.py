a = ((1,2),(3,4),(5,6))
print(a[0])
print(a[0][1])




# 문자열을 tuple로 타입변경
a_str = 'abcde'
# print(a_str)
# print(a_str[1])

a_tu = tuple(a_str) # 수정추가불가
list(a_tu)
print(list(a_tu))   # 수정 가능


### 두 수의 치ㅣ환 ###
# a = '우유'
# b = '커피'
# c = ''

# # 파이썬 a, b 치환
# print(a,b)
# a,b = b,a
# print(a,b)

# # 기본적인 a, b 치환
# print(a,b)
# a = b
# b = c
# c = a
# print()










# aArr = [[1,2],[[1,2],[3,4]],[5,6],[7,8]]
# a_list = [1,2,1,2,3,4,5,6,7,8]

# b_list = []
# for i in aArr:
#   if type(i) == list:
#     for j in i:
#       if type(j) == list:
#         for k in j:
#           b_list.append(k)
#       else:
#         b_list.append(j)
# print(b_list)





# t = (1,2,3,4)
# print(type(t))

# t = [3,5,1,2]
# t.sort()  # t가 변경됨
# print(t)
# t[1:3]  # t가 변경되지 않음

# t + [3,7] # t에 반영 안됨
# print(t + [3,7])  # t에 반영됨
# print(t)

# t.extend(t + [3,7]) # t에 반영되지 않음



### 튜플 - list타입과 같음. 순서가 있음.(i[0]) but 수정, 추가 불가 ###
# 괄호로 나옴

# t = (1,2,3,4)
# print(t)
# print(t[0])
# # t[0] = 100  # 튜플은 수정 불가. 에러남
# # t.append(100) # 추가하는 함수 사용도 불가. 에러남!
# print(len(t))
# print(t[0])
# # for문 가능
# for i in t:
#   print(i)

# # 더하기 연산자로 추가 가능
# t = t+(5,6)
# print(t)

# # 곱하기 연산자로 추가 가능
# tt = (1,2,3)
# tt = tt * 2 
# print(tt)

# tArr = [1,2,3,4]
# tArr[0] = 100
# print(tArr)