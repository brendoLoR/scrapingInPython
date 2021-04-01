from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

jobs = []

soup = BeautifulSoup(html_text, 'lxml')
tags = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for tag in tags:
    published_date = tag.find('span', class_ = 'sim-posted').text.replace('\r','').replace('\n','')
    if ('Posted few days ago' in published_date):
        apply_link = tag.find('h2').a['href']
        company_name = tag.find('h3', class_ = 'joblist-comp-name').text.replace(' ','').replace('\r','').replace('\n','')
        skills = tag.find('span', class_ = 'srp-skills').text.replace(' ', '').replace('\r','').replace('\n','')
        jobs.insert(0, [company_name, skills, published_date, apply_link])

print(jobs)