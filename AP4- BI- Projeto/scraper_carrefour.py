import requests
from bs4 import BeautifulSoup
import csv

# URL da busca por lava e seca
url = "https://www.carrefour.com.br/busca/lava%20e%20seca"

# Headers para simular navegador
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Requisição da página
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Lista de produtos
produtos = soup.find_all("li", class_="product-card")

# Lista para armazenar dados
dados = []

# Extração dos dados
for produto in produtos:
    nome = produto.find("h2", class_="product-card__title")
    preco = produto.find("span", class_="sales-price")
    link = produto.find("a", class_="product-card__link")
    
    nome = nome.text.strip() if nome else "N/A"
    preco = preco.text.strip() if preco else "N/A"
    link = f"https://www.carrefour.com.br{link['href']}" if link else "N/A"
    
    marca = nome.split()[0] if nome != "N/A" else "N/A"

    dados.append([nome, preco, link, marca])

# Salvar em CSV
with open("produtos_lavaeseca.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Nome do Produto", "Preço", "Link do Produto", "Marca"])
    writer.writerows(dados)

print("✅ Dados extraídos com sucesso! Verifique o arquivo produtos_lavaeseca.csv.")
