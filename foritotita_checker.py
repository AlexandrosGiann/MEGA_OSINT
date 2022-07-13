from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

os.environ['WDM_LOG_LEVEL'] = '0'
os.environ['WDM_LOCAL'] = '1'
chrome_options = webdriver.chrome.options.Options()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.foritotita.gr/?page_id=362"

browser.get(url)
phone_input = browser.find_element("name", "number")
phone_input.clear()
phone_input.send_keys("1234567890")

#recaptcha = browser.find_element("class", "g-recaptcha")
#recaptcha.click()

#submit = browser.find_element("name", "doVerify")
#submit.click()
# "role""checkbox" aria-checked="false" id="recaptcha-anchor" tabindex="0" dir="ltr" aria-labelledby="recaptcha-anchor-label"><div class="recaptcha-checkbox-border" role="presentation"></div><d"class","recaptcha-checkbox-borderAnimation""class","recaptcha-checkbox-spinner""class","recaptcha-checkbox-spinner-overlay"
# "src","https://www.google.com/recaptcha/api.js"
print([line for line in browser.execute_script("return document.documentElement.innerHTML;").split("<") if "sitekey" in line])
