from email.mime.text import MIMEText
from smtplib import SMTP_SSL

send_svr = SMTP_SSL('smtp.qq.com', 465)
fuser = 'xxxxxxxxxxx@qq.com' #mail address
tuser = 'xxxxxxxxxxx@qq.com'
send_svr.login(fuser, 'xxxxxxxxxxx') #auth code
msg = MIMEText( 'hello world python')
msg['Subject'] = 'test'
msg['From'] = fuser
msg['To'] = tuser
errs = send_svr.sendmail(fuser, [tuser], msg.as_string())
send_svr.quit()