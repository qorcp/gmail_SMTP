import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import codecs

def readFile(fileName, list):

    f = open(fileName, 'r') # read file
    lines = None # define variable
    try:
        lines = f.readlines() # try to read line by line
    except:
        f.close() # close the file if read file failed
        try:
            f =  codecs.open(fileName, 'r', 'UTF-8') # if the read file failed, try to read file with encoding utf-8
            lines = f.readlines() # read line by line
        except:
            try:
                f =  codecs.open(fileName, 'r', 'UTF-16') # if the read file failed with encoding utf-8, try to read file with encoding utf-16
                lines = f.readlines() # read line by line
            except:
                print("failed to read file") # all case is failed, print out

    f.close() # close file

    for line in lines:
        line = line.strip() # 줄바꿈 삭제
        list.append(line) # txt 파일 한줄씩 list에 저장


# 리스트 변수 선언
receiver = []
readFile(r'C:\SHARE\DOJA_UPD\0.program\email.txt', receiver) # 파일 경로 = 절대경로

# 리스트 변수 선언
log = []
readFile(r'C:\SHARE\DOJA_UPD\2.backup\4.log\update.log', log) # 파일 경로 = 절대경로

# 오늘 날짜 가져오기
today = datetime.today().strftime("%Y-%m-%d") # 날짜를 yyyy-MM-dd 형태로 출력

# 로그 변수에서 오늘 날짜 포함된 부분만 추출
matching = [i for i in log if today in i]

# 문자열 변수 선언
tempContent = ''

# 문자열에 문자 붙히기
for i in matching:
    tempContent += i + '\n'

#print(tempContent) # 붙혀진 문자 확인용

# 이메일 제목
message = MIMEMultipart()
message['Subject'] = str(today) + ' 셀별 파일 업로드 현황'

# 이메일 내용
content = MIMEText(tempContent)

# 이메일 제목 및 내용 병합
message.attach(content)

# SMTP 서버 정의
SMTP = smtplib.SMTP('smtp.gmail.com', 587) #587 = 포트번호
SMTP.starttls() # tls 방식으로 SMTP
SMTP.login("보내는 메일 주소 입력", "보내는 메일 주소 비번") # 보내는 메일 로그인

# 메일 보내기
for i in receiver:
    message['To'] = i
    SMTP.sendmail(receiver, i, message.as_string())
SMTP.quit()
print("메일 전송 완료")

