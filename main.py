import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login("pythoncode.maker@gmail.com", "1235912Gg*")

message= "Email sent via VS code python"

s.sendmail("pythoncode.maker@gmail.com", "elgrhy@aol.com", message)

s.quit()
