from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import re

os.environ['WDM_LOG_LEVEL'] = '0'
os.environ['WDM_LOCAL'] = '1'
chrome_options = webdriver.chrome.options.Options()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

for url in open('urls.txt', 'r').readlines():
    url = url.replace('\n', '')
    browser.get(url)
    code = browser.execute_script('return document.documentElement.innerHTML;')
    match = re.findall(r'[\w\.-]+@[\w\.-]+', code)
    print([email for email in match if email[-4:] == '.com'])
input('Press enter to exit...')
