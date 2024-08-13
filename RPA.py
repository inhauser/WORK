from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time


#Login Produção

#Seleção do driver para usar o Edge (Entender o porque não está funcionando o chrome)
options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)

#Acessar o link do LearningRocks
driver.get("https://azul.skore.io/login")
driver.maximize_window()
driver.implicitly_wait(2)

time.sleep(5)

#Clica no botão para fazer o login por SSO
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[1]/div/main/div[2]/div[2]/div/div/div/div[1]/button"""))).click()

#Ir para a tela de turmas
driver.get("https://azul.skore.io/spaces")


#Clica no botão de banco de questões
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[1]/div/div/main/div/div[2]/button[2]"""))).click()

#Clica no botão de questões
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[1]/div/div/main/div/div[3]/div[1]/button"""))).click()


dados = pd.read_excel('questões.xlsx')


def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH,xpath)
    except NoSuchElementException:
        return False
    return True

for a in range(0,len(dados)):

    #Clica no botão de Nível
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[1]/div/div/main/div/div[3]/div[5]/div/div[3]/div/div/div[2]/div/span"""))).click()

    #Clica na opção da questão
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[1]/div/div/main/div/div[3]/div[5]/div/div[3]/div/div/div[2]/ul/li["""+str(dados.at[a,'Nível'])+"""]"""))).click()

    elem = driver.find_element(By.XPATH, """/html/body/div[1]/div/div/main/div/div[3]/div[5]/div/div[3]/div/div/section/div[2]/div/input""")
    elem.clear()
    elem.send_keys(dados.at[a,'Tópico'])

    time.sleep(5)

    if check_exists_by_xpath("""/html/body/div[1]/div/div/main/div/div[3]/div[5]/div/div[3]/div/div/section/div[2]/div[2]/div[1]"""):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[1]/div/div/main/div/div[3]/div[5]/div/div[3]/div/div/section/div[2]/div[2]/div[2]/button"""))).click()
    else:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="__layout"]/div/main/div/div[3]/div[5]/div/div[3]/div/div/section/div[2]/ul/li"""))).click()

    time.sleep(1)
    #Colocar pergunta
    elem = driver.find_element(By.XPATH, """/html/body/div[1]/div/div/main/div/div[3]/div[5]/div/div[3]/div/main/div[1]/div/div[2]/textarea""")
    elem.clear()
    elem.send_keys(dados.at[a,'ENUNCIADO DA QUESTÃO'])

    time.sleep(1)
    #Colocar resposta correta
    elem = driver.find_element(By.XPATH, """/html/body/div[1]/div/div/main/div/div[3]/div[5]/div/div[3]/div/main/div[2]/div[1]/div/div/main/div[2]/div[2]/div/div[2]/textarea""")
    elem.clear()
    elem.send_keys(dados.at[a,'ALTERNATIVA CORRETA'])

    time.sleep(1)
    #Colocar outras respostas
    elem = driver.find_element(By.XPATH, """/html/body/div[1]/div/div/main/div/div[3]/div[5]/div/div[3]/div/main/div[2]/div[2]/div/div/main/div[2]/div[2]/div/div[2]/textarea""")
    elem.clear()
    elem.send_keys(dados.at[a,'ALTERNATIVA 1'])

    time.sleep(1)
    #Clica no botão para adicionar respostas
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[1]/div/div/main/div/div[3]/div[5]/div/div[3]/div/main/div[2]/div[3]/p"""))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[1]/div/div/main/div/div[3]/div[5]/div/div[3]/div/main/div[2]/div[4]/p"""))).click()

    time.sleep(1)
    #Colocar outras respostas
    elem = driver.find_element(By.XPATH, """/html/body/div[1]/div/div/main/div/div[3]/div[5]/div/div[3]/div/main/div[2]/div[3]/div/div/main/div[2]/div[2]/div/div[2]/textarea""")
    elem.clear()
    elem.send_keys(dados.at[a,'ALTERNATIVA 2'])

    time.sleep(1)
    #Colocar outras respostas
    elem = driver.find_element(By.XPATH, """/html/body/div[1]/div/div/main/div/div[3]/div[5]/div/div[3]/div/main/div[2]/div[4]/div/div/main/div[2]/div[2]/div/div[2]/textarea""")
    elem.clear()
    elem.send_keys(dados.at[a,'ALTERNATIVA 3'])

    time.sleep(1)
    #Clica para colocar a primeira opção como a certa
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[1]/div/div/main/div/div[3]/div[5]/div/div[3]/div/main/div[2]/div[1]/div/div/main/div[2]/div[1]/span"""))).click()
    
    time.sleep(1)
    #Clica no salvar
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[1]/div/div/main/div/div[3]/div[5]/div/div[4]/button[2]"""))).click()

    time.sleep(1)
    #Clica no botão de questões
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[1]/div/div/main/div/div[3]/div[5]/div/div[4]/button[2]"""))).click()


#Fechar navegador
driver.quit()


