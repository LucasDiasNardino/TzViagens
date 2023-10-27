from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def cvc(driver):
    driver.get("https://www.cvc.com.br/lp/promocoes/saldao-de-pacotes")

    try:
        driver.set_page_load_timeout(30)

        modalPacotes = driver.find_element(By.CLASS_NAME, "slick-track")

        driver.execute_script("arguments[0].scrollIntoView(true)", modalPacotes)

        #iterar pelos pacotes

            
        # Localize todos os elementos que representam pacotes
        pacotes = driver.find_elements(By.CLASS_NAME, "bloco-oferta-card")

        # Inicialize listas para armazenar as informações
        destinos = []
        valores = []

        # Itere pelos pacotes e colete informações
        for pacote in pacotes:
            destino = pacote.find_element(By.CLASS_NAME, "bloco-oferta-card-produto").text
            valor = pacote.find_element(By.CLASS_NAME, "bloco-oferta-card-rodape").text
            destinos.append(destino)
            valores.append(valor)

        # Agora você tem as informações de destino e valor dos pacotes em suas listas
        # Você pode imprimir ou usar essas informações conforme necessário
        for i in range(len(destinos)):
            print(f"Destino: {destinos[i]}, Valor: {valores[i]}")

    except TimeoutException:
        print("Timed out waiting for page to load")
        driver.quit()

def launch():

    driver = webdriver.Chrome()
    cvc(driver)
    while(True):
        pass

launch()