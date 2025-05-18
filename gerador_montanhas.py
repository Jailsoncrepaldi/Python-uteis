from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

# Configurar as opções do navegador para o modo headless
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Inicializar o navegador com as opções
driver = webdriver.Chrome(options=chrome_options)

# Acessar o site e definir o número de imagens que você deseja baixar
num_images_to_download = 5

for i in range(num_images_to_download):
    # Acessar o site
    driver.get("https://thismountaindoesnotexist.com/")

    # Encontrar a imagem usando XPath
    image = driver.find_element('xpath', '//*[@id="mountain"]')

    # Obter o URL da imagem
    image_url = image.get_attribute("src")

    # Nomear o arquivo com base no contador
    filename = f"pessoa_gerada_{i + 1}.jpg"

    # Baixar a imagem
    response = requests.get(image_url)
    with open(filename, "wb") as file:
        file.write(response.content)

# Fechar o navegador
driver.quit()
