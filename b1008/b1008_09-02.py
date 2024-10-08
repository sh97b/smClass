students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']
no = len(students)+1
choice = 0 # 전역변수
chk = 0    # 체크변수
count = 1  # 성적처리
stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 #성적처리변수

# 학생성적프로그램

while True:
  print("                    [ 학생성적프로그램 ]")
  print("-" * 60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("0. 프로그램 종료")
  print("-" * 60)

  choice = input("원하는 번호를 입력하세요 >> ")

  if choice == '1':
    while True:
      print("\n                    [ 학생성적입력 ]")
      name = input(f"{no}번째 학생의 이름을 입력하세요. (입력 취소 : 0) >> ")
      if name == '0':
        print("성적 입력을 취소합니다.\n")
        break  # 한번 빠져나옴
      kor = int(input("국어 성적을 입력하세요. >> "))
      eng = int(input("영어 성적을 입력하세요. >> "))
      math = int(input("수학 성적을 입력하세요. >> "))
      total = kor + eng + math
      avg = total / 3
      rank = 0

      ss = {
        'no':no, 'name':name, 'kor':kor, 'eng':eng, 'math':math, 'total':total, 'avg':avg, 'rank':rank
      }
      students.append(ss) ### 딕셔너리로 저장 ###
      
      print(f"번호 : {no}\t이름 : {name}\t국어 : {kor}\t영어 : {eng}\t수학 : {math}\t합계 : {total}\t평균 : {avg:.2f}\t등수 : {rank}\t")
      print(f"\n{name}학생의 성적이 저장되었습니다.")

      no += 1
    print("프로그램을 종료합니다\n")

  elif choice == '2':
    print("\n                    [ 학생성적출력 ]")

    # 상단 타이틀 출력
    for title in s_title:
      print(f"{title}",end='\t')
    print()
    print("-" * 60)

    # 학생성적출력
    for s in students:
      print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}등\t")
    print()
    

  elif choice == '3':
    print("\n                    [ 학생성적수정 ]")
    name = input("수정하고자 하는 학생의 이름을 입력하세요. >> ")
    for s in students:
      if s[1] == name:
        print(f"{name}학생을 찾았습니다.")

        print("[수정 과목 선택]")
        print("1. 국어 성적 수정")
        print("2. 영어 성적 수정")
        print("3. 수학 성적 수정")
        print("0. 수정 취소")
        
        choice = input("원하는 번호를 선택하세요. (수정 취소 : 0) >> ")
        if choice == '1':
          print("현재 국어 점수 : {}".format(s[2]))
          s[2] = int(input("변경 국어 점수 >> "))
        elif choice == '2':
          print("현재 영어 점수 : {}".format(s[3]))
          s[3] = int(input("변경 영어 점수 >> "))
        elif choice == '3':
          print("현재 수학 점수 : {}".format(s[4]))
          s[4] = int(input("변경 수학 점수 >> "))
        elif choice == '0':
          print("수정을 취소합니다.")
          chk = 1

        if choice != '0':
          s[5] = s[2] + s[3] + s[4]   # 합계 수정
          s[6] = s[5] / 3             # 평균 수정
          print(f"{name} 학생의 성적이 수정되었습니다.")
          chk = 1

    if chk == 0:
      print("찾고자 하는 학생이 없습니다.\n")

  elif choice == '4':
    print("\n                    [ 학생성적검색 ]")
    name = input("찾고자 하는 학생의 이름을 입력하세요. >> \n")

    chk = 0
    for s in students:
      if s[1] == name:
        print(f"{name} 학생을 찾았습니다.")
        # 상단
        for title in s_title:
          print(f"{title}", end='\t')
        print()
        print("-" * 60)

        # 하단
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}등\n")
        chk = 1
        break
    
    # 모든 학생의 비교가 끝난 후에 chk 확인
    if chk == 0:
      print(f"{name} 학생이 없습니다.\n")

  elif choice == '5':
    print("\n                    [ 학생성적삭제 ]")
    name = input("찾고자 하는 학생의 이름을 입력하세요. >> \n")
    chk = 0

    for idx, s in enumerate(students):
      if s[1] == name:
        choice = input(f"{name} 학생의 성적을 삭제하시겠습니까? (삭제 시 복구 불가)\n1. 삭제\n2. 취소")
        if choice == '1':
          del students[idx]
          print(f"{name} 학생의 성적이 삭제되었습니다.")
        else:
          print("삭제가 취소되었습니다.")
        chk = 1

    if chk == 0:
      print(f"{name} 학생이 없습니다.\n")

  elif choice == '6':
    print("\n                    [ 등수처리 ]")
    for s in students:
      count = 1
      for st in students:
        if s[5] < st[5]:
          count += 1
      s[7] = count  # 등수입력

    print("등수처리가 완료되었습니다.\n")

  elif choice == '0':
    print("\n                    [ 프로그램을 종료합니다. ]")






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
