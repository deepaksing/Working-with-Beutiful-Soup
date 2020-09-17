from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://codeforces.com/contests"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

cont = soup.find_all('table')[0]
conth = cont.find_all('tr')

contest_names = []
contest_start = []
contest_time = []
contest_before_start = []


for i in range(1, len(conth)):
	contn = conth[i].find_all('td')[0]
	conts = conth[i].find_all('td')[2]
	contt = conth[i].find_all('td')[3]
	contbs = conth[i].find_all('td')[4]

	contest_names.append(contn.get_text())
	contest_start.append(conts.get_text())
	contest_time.append(contt.get_text())
	contest_before_start.append(contbs.get_text())

contest = pd.DataFrame({
    "name": contest_names,
    "Start Time": contest_start,
    "Duration": contest_time,
    "Before Start":contest_before_start
})


contest.to_csv(r'C:\Users\Deepak\Desktop\Working-with-Beutiful-Soup\contests.csv', header=True, index=False) 
