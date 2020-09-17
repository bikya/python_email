#Importing SMTP Library
import smtplib
#Connecting to any smtp mail server and their port
conn = smtplib.SMTP('smtp.gmail.com', 587)
#Identifying Self Before Connecting
conn.ehlo()
#Starting Encrypted Connection using TLS to send securely
conn.starttls()
#Login using Username and Password(Use Application Specific Password
conn.login('<username>','<pass>')
#Writing From,To,Subject as per traditional mail
conn.sendmail('<from>','<to>','Subject:\n\n ***HERE GOES DATA ***');
#Close the connection
conn.quit()
