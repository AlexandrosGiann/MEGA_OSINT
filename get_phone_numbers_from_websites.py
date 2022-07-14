from pnt1 import get_phone_number_info
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import warnings
warnings.filterwarnings("ignore")

os.environ['WDM_LOG_LEVEL'] = '0'
os.environ['WDM_LOCAL'] = '1'
chrome_options = webdriver.chrome.options.Options()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

def count_numbers(text):
    return sum([text.count(str(i)) for i in range(10)])

def contains_characters(text):
    return True in [c.isalpha() for c in text]

def get_phone_numbers(text):
    text = ''.join([c for c in text if not c.isalpha()])
    text = text.replace('<', '\n')
    text = text.replace('>', '\n')
    text = text.replace(' ', '-')
    text = text.replace('(', '-')
    text = text.replace(')', '-')
    text = text.replace('.', '-')

    lst = []
    
    for line in text.split("\n"):
        if count_numbers(line) > 4:
            element = line.split('-')
            out = ""
            while element[0] == '':
                element = element[1:]
            last = ''
            while element:
                if element[0]:
                    if element[0][0] == '+':
                        out += element[0] + ' '
                    elif element[0].isnumeric():
                        out += element[0]
                    else:
                        if '+' not in last:
                            lst.append(out)
                            out = element[0]
                else:
                    if '+' not in last:
                        lst.append(out)
                        out = element[0]
                last = element[0]
                element = element[1:]
            if out:
                lst.append(out)
    lst = [l for l in lst if l and not contains_characters(l)]
    lst1 = []
    for l in lst:
        try:
            if get_phone_number_info(l, '1'):
                lst1.append(l)
                print(l)
        except:
            pass
    return lst1
            
def GPNFW():
    lst = []
    for url in open('urls.txt', 'r').readlines():
        url = url.replace('\n', '')
        browser.get(url)
        code = browser.execute_script('return document.documentElement.innerHTML;')
        for phone_number in get_phone_numbers(code):
            if phone_number not in lst:
                lst.append(phone_number + '\n')
    file = open('result_phone_numbers.txt', 'w')
    file.writelines(lst)
    file.close()

if __name__ == '__main__':
    GPNFW()

