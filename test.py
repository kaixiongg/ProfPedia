# -*- coding: utf-8 -*-


from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import re
import codecs

def univNama(tag):
    return tag.name == u'td' and len(tag.attrs) == 0

aiAreas = {"ai", "vision", "ml", "nlp", "web+ir"}
systemsAreas = {"arch", "mobile", "security", "eda", "db", "mobile", "metrics", "se", "embedded", "hpc", "os", "pl","networks"}
theoryAreas = {"theory", "crypto", "logic"}
interdisciplinaryAreas = {"graphics", "hci", "robotics", "bio", "visualization", "ecom"}


browser = webdriver.Chrome()
browser.get('http://csrankings.org/')
browser.find_element_by_id('all_areas_off').click()
time.sleep(1)
browser.find_element_by_id('ai').click()
time.sleep(1)
browser.find_element_by_id('Carnegie%20Mellon%20University-widget').click()
time.sleep(1)
soup = BeautifulSoup(browser.page_source, "html.parser")
# file = open("html_CMU", "w")
# file.write(soup.prettify('latin-1'))
fileLink = open("CMU1", "w")
"""the name and related link"""
# for link in soup.find_all("a"):
#     print link.text, link.get("href")
data = str()
for link in soup.find_all(univNama):
    data += str(link.text.encode('utf-8')).replace('\n',' ')
# print(data)

data = re.sub(r'►','#',data)
# data = re.sub(r'','#',data)
data = re.sub(r'Faculty', '@',data)

data = re.sub(r'[^A-Za-z0-9!@#\$%\^&\.\,\|\?\'\:\*\(\)\+ ]+', r' ', data)
# data = re.sub(r'\'', r'\\'', data)

data= re.sub(r'(\s+)',r' ', data)

# print(data)
data = data.replace('Carnegie', '# Carnegie')
data = data.replace('#','\n#')



name = re.findall(r'(?<=#)(.*)(?=@)',data)
prof = re.findall(r'(?<=@)(.*)(?=)',data)

for i in range(len(name)):
    f= open('universities/'+name[i] , 'w+')
    f.write(prof[i])
    f.close()



# data.replace('▼','#')
# print(data)
# for i in range(1,200):
#     r'(?<=% of )(.*)(?= at )'