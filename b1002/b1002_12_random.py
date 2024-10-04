# 랜덤숫자 생성 (js의 Math.random과 동일)
# 0 <= x <1 실수값 추출
import random

print(random.random())

# 자바, 자바스크립트는 이렇게햇엇음
# 0-9
print(int(random.random() * 10))
# 0-10
print(int(random.random() * 10)+1)


# randint - 랜덤 int 추출 (n부터, m까지(m포함))
print(random.randint(1,10))

# randrange - 랜덤 범위 추출 (n부터, m앞전까지)
print(random.randrange(1,3))

# choice - 리스트에서 랜덤 추출
a = [1,4,5,9]
print(random.choice(a))

# choices - 리스트에서 여러 개 랜덤 추출(중복 가능)
print(random.choices(a, k=2))

# sample - 리스트에서 여러 개 랜덤 추출(중복 불가)
print(random.sample(a,2))