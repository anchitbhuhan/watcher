import psutil
import smtplib
#Get CPU Usage
cpu_usage = psutil.cpu_percent(interval=1)
#Get Memory Usage
memory_usage = psutil.virtual_memory().percent
#Get Disk Usage
disk_usage = psutil.disk_usage('/').percent
print(f"CPU Usage: {cpu_usage}%")
print(f"Memory Usage: {memory_usage}%")
print(f"Disk Usage: {disk_usage}%")

def send_email(subject, message):
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('anchit626@gmail.com', "rhhluqwhauocxmbt")
        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail('anchit626@gmail.com', 'rishabhkhemka1525@gmail.com', email_message)

if cpu_usage > 0:
    send_email("CPU Usage : ", f"CPU Usage is at {cpu_usage}%!")
    print("Mail Sent")
