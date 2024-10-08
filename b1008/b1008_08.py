import copy

name = ['홍길동','유관순','이순신']
score = [100,90,95]

ns_dic = dict(zip(name,score))
# print(ns_dic)

# a = ns_dic  # 얕은복사
a = copy.deepcopy(ns_dic)

a['홍길동'] = 0
print(ns_dic)
print(a)



### 얕은복사 / 깊은복사 ###

# ### 얕은복사
# name = ['홍길동','유관순','이순신']

# n = name  # name의 값을 n에 복사
# n[2] = '김구' # 이순신 -> 김구
# print(n)  
# print(name) # n[2]를 변경했는데 name[2]도 변함

# ### 깊은복사
# name = ['홍길동','유관순','이순신']

# n = name[:]
# n[2] = '김구' 
# print(n)  # n[2]만 변경됨
# print(name) # 얘 값은 그대로