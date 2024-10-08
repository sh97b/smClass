students = []
s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
no = 1
rank = 0
count = 0

while True:
  print("\n[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("0. 프로그램 종료")
  print("-"*60)

  choice = input("원하는 번호를 입력하세요(0.종료)>> ")

  if choice == '1':
    while True:
      print("\n[ 학생성적입력 ]")
      print("-" * 60)
      name = input(f"{no}번째 학생의 이름을 입력하세요(입력 취소 : 0) >> ")
      if name == '0':
        print("입력을 취소합니다.")
        break
      kor = int(input("국어 점수를 입력하세요 >> "))
      eng = int(input("영어 점수를 입력하세요 >> "))
      math = int(input("수학 점수를 입력하세요 >> "))
      total = kor + eng + math
      avg = total / 3
      
      print(f"번호 : {no}\t이름 : {name}\t국어 : {kor}\t영어 : {eng}\t수학 : {math}\t합계 : {total}\t평균 : {avg:.2f}\t등수 : {rank}\t")
      print(f"{name} 학생의 성적이 저장되었습니다.")

      s = [no, name, kor, eng, math, total, avg, rank]
      students.append(s)
      no += 1
    print("\n[ 프로그램을 종료합니다. ]")

  elif choice == '2':
    print("\n[ 학생성적출력 ]")
    print("-" * 60)

    # 상단 출력
    for title in s_title:
      print(title, end='\t')    
    print()
    print("-" * 60)
    
    # 하단 출력
    for s in students:
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\t")
    print()

  elif choice == '3':
    print("[ 학생성적수정 ]")
    name = input("수정하고자 하는 학생의 이름을 입력하세요 >> ")
    for s in students:
      if name == s[1]:
        print(f"{name} 학생을 찾았습니다.")

        print("[ 수정 과목 ]")
        print("1. 국어 성적")
        print("2. 영어 성적")
        print("3. 수학 성적")
        print("0. 수정 취소")

        choice = input("원하는 번호를 입력하세요(취소 : 0) >> ")
        if choice == '1':
          print("[ 국어 성적 수정 ]")
          print(f"현재 국어 점수 : {s[2]}")
          s[2] = int(input("변경하려는 국어 점수 >> "))
        elif choice == '2':
          print("[ 영어 성적 수정 ]")
          print(f"현재 영어 점수 : {s[3]}")
          s[3] = int(input("변경하려는 영어 점수 >> "))
        elif choice == '3':
          print("[ 수학 성적 수정 ]")
          print(f"현재 수학 점수 : {s[4]}")
          s[4] = int(input("변경하려는 수학 점수 >> "))
        elif choice == '0':
          print("수정을 취소합니다.")
          count = 1
    
        if choice != '0':
          s[5] = s[2] + s[3] + s[4]
          s[6] = s[5] / 3
          print(f"{name} 학생의 성적이 수정 완료되었습니다.")
          count = 1
    
    if count == 1:
      print("찾고자 하는 학생이 없습니다.")

  else:
    print("\n[ 프로그램을 종료합니다. ]")
    break