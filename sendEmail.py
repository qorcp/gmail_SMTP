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
        line = line.strip() # delete new line
        list.append(line) # add txt file content line by line into the list


# declare array
receiver = []
readFile(r'your txt file with email address path', receiver) # txt file with email address(absolute path)

# declare array
log = []
readFile(r'your log file path', log) # log file path(absolute path)

# get today's date
today = datetime.today().strftime("%Y-%m-%d") # yyyy-MM-dd

# Extract only the part containing today's date from the "log" array
matching = [i for i in log if today in i]

# string variable declaration
tempContent = ''

# pasting characters into a string
for i in matching:
    tempContent += i + '\n'

#print(tempContent) # For checking pasted characters

# title of email
message = MIMEMultipart()
message['Subject'] = str(today) + ' 셀별 파일 업로드 현황'

# content of email
content = MIMEText(tempContent)

# merge the title and content of email
message.attach(content)

# SMTP
SMTP = smtplib.SMTP('smtp.gmail.com', 587) #587 = port number
SMTP.starttls() # tls 방식으로 SMTP
SMTP.login("your email address", "your email password") # Outgoing mail login. In this case, your email

# send email to many people
for i in receiver:
    message['To'] = i
    SMTP.sendmail(receiver, i, message.as_string())
SMTP.quit()
print("complete sending email")

