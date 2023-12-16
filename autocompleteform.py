from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='/usr/bin/chromedriver')



options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
messageField = driver.find_element("xpath", '/html/body/form/div[2]/div[4]/input')
messageField.send_keys('Hello World')
lastnameField = driver.find_element("xpath", '//*[@id="RESULT_TextField-2"]')
lastnameField.send_keys("2024")
