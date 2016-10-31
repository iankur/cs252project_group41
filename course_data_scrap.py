import httplib2
import csv
import requests
from bs4 import BeautifulSoup, SoupStrainer

http = httplib2.Http()
url_to_scrape = 'http://cse.iitk.ac.in'
status, response = http.request('http://cse.iitk.ac.in/pages/Courses.html')
courses_links = []
for a_Tag in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')).find_all('a', href=True):
	if ('../pages/CS' in a_Tag['href'] or '../pages/ESC' in a_Tag['href']) and not ('CSE' in a_Tag['href']):
		relative_link_to_course_details = a_Tag['href'][2:]
		absolute_link_to_course_details = url_to_scrape + relative_link_to_course_details
		courses_links.append(absolute_link_to_course_details)

courses = []

for course_link in courses_links[:10]:
	r = requests.get(course_link)
	soup = BeautifulSoup(r.text)
	
	course_details = []
	for course_data in soup.select('.page'):
		h1 = len(course_data.findAll('h1'))
		h2 = len(course_data.findAll('h2'))
                h3 = len(course_data.findAll('h3'));
                h4 = len(course_data.findAll('h4'));
                h5 = len(course_data.findAll('h5'));
                h6 = len(course_data.findAll('h6'));
                p = len(course_data.findAll('p'));
		ol = len(course_data.findAll('ol'));
		k = ''
                course_details.append(k)
		course_details.append(k)
		course_details.append(k)
                course_details.append(k)
		if ol > 0 :
			course_content = []
                        li = len(course_data.findAll('ol')[0].findAll('li'))
                        for k in range(0,li):
				course_details[3] = course_details[3] + "\n" + course_data.findAll('li')[k].text.strip()
		
		for k in range(0,h5) :
			if 'Units:' in course_data.findAll('h5')[k].text.strip() :
				course_details[2] = course_data.findAll('h5')[k].text.strip()
		for k in range(0,p) :
			if 'Units:' in course_data.findAll('p')[k].text.strip() :
				course_details[2] = course_data.findAll('p')[k].text.strip()
		for k in range(0,h5) :
			if 'Pre-re' in course_data.findAll('h5')[k].text.strip() :
				course_details[1] = course_data.findAll('h5')[k].text.strip()
		for k in range(0,p) :
			if 'Pre-re' in course_data.findAll('p')[k].text.strip() :
				course_details[1] = course_data.findAll('p')[k].text.strip()  
		if h1 > 0 :	
			course_details[0] = course_data.findAll('h1')[0].text.strip()
		elif h2 > 0:
			course_details[0] = course_data.findAll('h2')[0].text.strip()
		elif p > 0:
			course_details[0] = course_data.findAll('p')[0].text.strip()
		
		              			
		print  course_details[0]
		print course_details[2]
		print course_details[1]
		print 'Content : ' + course_details[3][:]
	
	courses.append(course_details)	
with open ('data.csv','wb') as file:
   writer=csv.writer(file)
   writer = csv.writer(file, delimiter = '$')
   for row in courses:
      writer.writerow([row])
