stu_title = ['번호', '이름', '국어', '영어', '수학', '과학', '합계', '평균']
stu_datas = [
 [1, "홍길동", 100, 100, 100, 99],
 [2, "유관순", 99, 99, 100, 99],
 [3, "이순신", 100, 99, 98, 99], 
 [4, "김구", 80, 100, 90, 99],
 [5, "김유신", 80, 100, 90, 99]
]


print("                     [학생성적프로그램]\n")

for s_t in stu_title:
  print("{}".format(s_t), end='\t')
print()
print("-" * 62)

for s_d in stu_datas:
  total = s_d[2] + s_d[3] + s_d[4] + s_d[5]
  avg = total / 4
  print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(s_d[0], s_d[1], s_d[2], s_d[3], s_d[4], s_d[5], total, avg))
print()
print("-" * 62)