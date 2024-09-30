stu_title = ['번호', '이름', '국어', '영어', '수학', '과학', '합계', '평균']
stu_datas = [
 [1, "홍길동", 100, 100, 100, 99],
 [2, "유관순", 99, 99, 100, 99],
 [3, "이순신", 100, 99, 98, 99], 
 [4, "김구", 80, 100, 90, 99],
 [5, "김유신", 80, 100, 90, 99]
]


# 내맘대루
print("                     [학생성적프로그램]\n")
print("-"*62)
#append - 합계, 평균 추가해서 출력
for s_d in stu_datas:
  total = s_d[2] + s_d[3] + s_d[4] + s_d[5]
  avg = total / 4
  s_d.append(total)
  s_d.append(avg)
  print(s_d)
print("-"*62)


# 쌤이랑 같이
print("                     [학생성적프로그램]\n")
print("-"*62)
#append - 합계, 평균 추가해서 출력
for s in stu_datas:
  s.append(s[2]+s[3]+s[4]+s[5])
  s.append((s[2]+s[3]+s[4]+s[5])/4)
  print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t")
print("-"*62)