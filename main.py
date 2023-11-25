import time
from nomes import nome
from nomes import sobrenomes
import random
import string
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from random_username.generate import generate_username
from senha import senha


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)

navegador.get('https://www.google.com/account/about/')
time.sleep(1)
navegador.find_element('xpath', '/html/body/header/div[1]/div[5]/ul/li[1]/a').click()
time.sleep(1)
#navegador.find_element('xpath', '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/button').click()
#time.sleep(1)
#navegador.find_element('xpath', '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/ul/li[1]').click()
#time.sleep(1)
navegador.find_element('xpath', '//*[@id="firstName"]').send_keys(random.choice(nome))
time.sleep(1)
navegador.find_element('xpath', '//*[@id="lastName"]').send_keys(random.choice(sobrenomes))
time.sleep(1)
navegador.find_element('xpath', '//*[@id="collectNameNext"]/div/button').click()
time.sleep(1)
navegador.find_element('xpath', '//*[@id="day"]').send_keys(10)
time.sleep(1)
navegador.find_element('xpath', '//*[@id="month"]').click()
time.sleep(1)
navegador.find_element('xpath', '//*[@id="month"]/option[4]').click()
time.sleep(1)
navegador.find_element('xpath', '//*[@id="year"]').send_keys(1995)
time.sleep(1)
navegador.find_element('xpath', '//*[@id="gender"]').click()
time.sleep(1)
navegador.find_element('xpath', '//*[@id="gender"]/option[4]').click()
time.sleep(1)
navegador.find_element('xpath', '//*[@id="birthdaygenderNext"]/div/button').click()
time.sleep(2)

email = generate_username()
pathEmail = ('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div[1]/div/div[1]/div/div[1]/input')
navegador.find_element('xpath', pathEmail).send_keys(email)
if navegador.find_element('xpath', pathEmail).send_keys((email)) == False:
    navegador.find_element('xpath', pathEmail).send_keys(email)

print(email)

navegador.find_element('xpath', '//*[@id="next"]/div/button').click()
time.sleep(2)

navegador.find_element('xpath', '//*[@id="passwd"]/div[1]/div/div[1]/input').send_keys(senha)
time.sleep(1)
navegador.find_element('xpath', '//*[@id="confirm-passwd"]/div[1]/div/div[1]/input').send_keys(senha)
senha1 = senha
print(senha1)
time.sleep(1)

navegador.find_element('xpath', '//*[@id="createpasswordNext"]/div/button').click()