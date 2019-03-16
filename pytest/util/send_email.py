import smtplib
from email.mime.text import MIMEText
class sendMeail():
    global send_user
    global password
    global email_host
    send_user = "邮箱账号@139.com"
    password = "邮箱密码"
    email_host = "smtp.139.com"
    def send_email(self,user_list,sub,context):
        user = "账号名"+"<"+send_user+">"
        message = MIMEText(context,_subtype="plain",_charset="utf-8")
        message["Subject"] = sub
        message["From"] = user
        message["To"] = ";".join(user_list)
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user,password)
        server.sendmail(user,user_list,message.as_string())
        server.close()

    def send_main(self,pass_count,fail_count):
        pass_num = float(len(pass_count))
        fail_num = float(len(fail_count))
        count_num = pass_num+fail_num
        pass_probability = "%.2f%%"%(pass_num/count_num*100)
        fail_probability = "%.2f%%"%(fail_num/count_num*100)
        user_list = ["收件箱账号@qq.com"]
        sub = "接口自动化测试报告"
        context = "此次共执行%s个用例，通过%s个，通过 率%s，不通过%s个，不通过率%s"%(count_num,pass_num,pass_probability,fail_num,fail_probability)
        self.send_email(user_list,sub,context)


