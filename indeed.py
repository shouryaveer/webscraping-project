from bs4 import BeautifulSoup
import requests
import lxml

print("****Indeed Quick Job Search****")
input_field = input("Enter job title: ")
loc = input("Enter job location: ")
j_dict = {'q': input_field, 'l': loc}
print("processing your request...")
r1 = requests.get('https://in.indeed.com/jobs', params=j_dict)
print(r1.url)
html_text = requests.get(r1.url).text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('span', class_ = 'company')

print("Companies with current openings for {} jobs at {}:".format(j_dict['q'], j_dict['l']))
for job in jobs:
    j_str = job.text
    print(j_str.replace('\n',''))