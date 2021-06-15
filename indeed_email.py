from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import getpass

print("****Indeed Quick Job Search****")
input_field = input("Enter job title: ")
loc = input("Enter job location: ")
j_dict = {'q': input_field, 'l': loc}
print("processing your request...")
r1 = requests.get('https://in.indeed.com/jobs', params=j_dict)
print("processing url:",r1.url, "\n")
html_text = requests.get(r1.url).text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('span', class_ = 'company')
j = []
for job in jobs:
    j_str = job.text.replace('\n','').rstrip()
    j.append(j_str)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    print("***Sign in to your Gmail Account to send an email to yourself: \n")
    email_id = input("Enter email address: ")
    email_pass = getpass.getpass(prompt='Enter password: ')

    smtp.login(email_id, email_pass)
    subject = 'Your List of companies with Job openings'
    body = "Here's your List of companies for {} job openings at {}:\n\n".format(j_dict['q'], j_dict['l']) + '\n'.join(j)
    msg = "Subject: {}\n\n{}".format(subject, body)
    smtp.sendmail(email_id, email_id, msg)

print("Email sent successfully. Check your inbox.")