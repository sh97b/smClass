students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']
no = len(students)+1

# 학생성적프로그램
while True:
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("7. 학생성적정렬") ######
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.(0.종료)>> ")

  if choice == '2':
    print("[ 학생성적출력 ]")
    
    # 상단 타이틀 출력
    for title in s_title:
      print(f"{title}",end='\t')
    print()
    print("-" * 60)
    # print(f"{s_title[0]}\t{s_title[1]}\t{s_title[2]}\t{s_title[3]}\t{s_title[4]}\t{s_title[5]}\t{s_title[6]}\t{s_title[7]}\t")

    for s in students:
      print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}등\t")
    print()
  elif choice == '7':
    while True:
      print("[ 학생성적정렬 ]")
      print("-" * 60,"\n")
      print("1. 이름으로 순차정렬")
      print("2. 이름으로 역순정렬")
      print("3. 합계로 순차정렬")
      print("4. 합계로 역순정렬")
      print("5. 번호 순차정렬")
      print("0. 이전페이지로")
      print("-" * 60)

      choice = input("원하는 번호를 입력하세요 >> ")

      if choice == '1':
        print("[ 이름으로 순차정렬 ]")
        students.sort(key=lambda x:x['name'])
      elif choice == '2':
        print("이름으로 역순정렬")
        students.sort(key=lambda x:x['name'],reverse=True)
      elif choice == '0':
        print("[ 이전페이지로 이동 ]")
        break
      
      print("[ 정렬 완료 ]")







# 학생성적 입력부분을 구현하시오
# dict 타입으로 입력
# 번호, 이름, 국어, 영어, 수학, 합계, 평균, 등수
# 입력 후 출력

# students = []
# s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
# no = 1

# while True:
#   name = input("이름을 입력하세요(취소 : 0) >> ")
#   if name == '0':
#     break
#   kor = int(input("국어 점수를 입력하세요 >> "))
#   eng = int(input("영어 점수를 입력하세요 >> "))
#   math = int(input("수학 점수를 입력하세요 >> "))
#   total = kor + eng + math
#   avg = total / 3
#   rank = 0

#   s = [no, name, kor, eng, math, total, avg, rank]
#   s_dic = dict(zip(s_title, s))
#   print(s_dic)