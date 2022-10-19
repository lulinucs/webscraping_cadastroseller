from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep


options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/lulifer/AppData/Local/Google/Chrome/User Data")
options.add_argument('--profile-directory=Profile 1')
driver = webdriver.Chrome(options=options)

print('esperando')
sleep(2)

arquivo_isbns = open("isbns.txt","r")
arquivo_precos = open("precos.txt","r")
arquivo_quantidades = open("quantidades.txt", "r")
isbn = arquivo_isbns.readlines()
preco = arquivo_precos.readlines()
quantidades = arquivo_quantidades.readlines()

linhas = len(isbn)
i=0

while i < linhas:
    try:
         driver.get("https://sellercentral.amazon.com.br/product-search?ref=xx_catadd_dnav_xx")
         sleep(1)
         busca = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[1]/div/div/div[1]/div/div/kat-input-group/kat-input')
         print('achei o campo de busca')
         busca.send_keys(isbn[i] + Keys.ENTER)
         print('--- Procurando produto ---')
         print('--- Verificando se o produto está na Amazon ---')
         sleep(1)
         verifica = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/div[1]")
         if verifica.text == "Displaying 0-0 of 0 results":
             print('Produto não cadastrado na Amazon. Pulando para o próximo item.')
             i += 1
         else:
             print('--- Item localizado ---')
             sleep(1)
             driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div/kat-box/div/section[3]/div[1]/section[2]/div/div/span[1]/kat-dropdown").send_keys(Keys.DOWN + Keys.ENTER)
             sleep(3)
             print('selecionei que quero vender um novo')
             driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div/kat-box/div/section[3]/div[1]/section[2]/div/div/span[2]/a").send_keys(Keys.ENTER)
             sleep(3)
             driver.switch_to.window(driver.window_handles[1])
             print(driver.current_url)
             sleep(3)
             driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[4]/section/div/div/section[2]/kat-input-group/kat-input").send_keys(preco[i])
             driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[7]/section/div/section[2]/kat-input").send_keys(quantidades[i] + Keys.TAB + Keys.DOWN + Keys.DOWN + Keys.ENTER)
             sleep(6)
             driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/kat-popover-trigger/kat-button").send_keys(Keys.ENTER)
             print('acho que foi tudo')
             sleep(10)
             driver.close()
         
             i += 1
    except:
        print('Algo deu errado, vou tentar novamente!')
        driver.switch_to.window(driver.window_handles[0])
    

driver.quit()