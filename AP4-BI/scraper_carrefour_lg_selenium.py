from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
import time

# Configuração do navegador headless
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Inicializar navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Acessar a página do produto
url = "https://www.carrefour.com.br/lava-e-seca-smart-lg-vc4-12kg-branca-com-inteligencia-artificial-aidd-cv5012wc4-220v-3410862/p"
driver.get(url)
time.sleep(5)  # Esperar o carregamento da página

# Coletar dados com Selenium
try:
    nome = driver.find_element(By.CSS_SELECTOR, "h1.product-name--title").text.strip()
except:
    nome = "N/A"

try:
    preco_inteiro = driver.find_element(By.CLASS_NAME, "product-sales-price__integer").text.strip()
    preco_decimal = driver.find_element(By.CLASS_NAME, "product-sales-price__fraction").text.strip()
    preco = f"R$ {preco_inteiro},{preco_decimal}"
except:
    preco = "N/A"

try:
    sku = driver.find_element(By.CLASS_NAME, "product-sku").text.strip()
except:
    sku = "N/A"

try:
    disponibilidade = driver.find_element(By.CLASS_NAME, "product-availability__status").text.strip()
except:
    disponibilidade = "N/A"

try:
    imagem = driver.find_element(By.CSS_SELECTOR, "img.product-image__img").get_attribute("src")
except:
    imagem = "N/A"

driver.quit()

# Salvar em CSV
with open("product_lg.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Nome do Produto", "Preço", "Referência", "Disponibilidade", "Imagem URL"])
    writer.writerow([nome, preco, sku, disponibilidade, imagem])

print("✅ Dados salvos com sucesso!")
