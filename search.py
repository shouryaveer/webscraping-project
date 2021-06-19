from bs4 import BeautifulSoup
import requests
import lxml

print("****Welcome to Quick Job Search****")
platform = input("Which job portal you want to search?\nPress 1 for LinkedIn,\nPress 2 for Indeed\n: ")
input_field = input("Enter job title: ")
loc = input("Enter job location: ")
if platform == '1':
    print("Checking LinkedIn for Companies with {} jobs".format(input_field))
    j_dict = {'keywords': input_field, 'location': loc, 'position': 1, 'pageNum': 0, 'distance': 50}
    r1 = requests.get('https://www.linkedin.com/jobs/search', params=j_dict)
    print("processing url:",r1.url)
    html_text = requests.get(r1.url).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('h4', class_ = 'base-search-card__subtitle')
else:
    j_dict = {'q': input_field, 'l': loc}
    print("processing your request...")
    r1 = requests.get('https://in.indeed.com/jobs', params=j_dict)
    print("processing url:",r1.url)
    html_text = requests.get(r1.url).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('span', class_ = 'company')
print("******************************************************************")
print("Companies with job openings for {} jobs at {}:".format(input_field, loc))
for job in jobs:
    j_str = job.text
    print(j_str.replace('\n',''))
