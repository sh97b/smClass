import datetime

today = datetime.datetime.now() # 날짜, 시간, 밀리초
nowDate = today.strftime("%Y-%m-%d")  # 날짜 포맷
nowDateTime = today.strftime("%Y-%m-%d %H:%M:%S")

print(today)  # 2024-10-08 17:58:47.592241
print(nowDate) # 24-10-08
print(nowDateTime) # 2024-10-08 18:03:25

print(type(today),"\t",type(nowDate),"\t",type(nowDateTime))