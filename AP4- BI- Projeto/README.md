# Web Scraping Carrefour - Lava e Seca

Este projeto consiste em uma aplicação Python que realiza **web scraping** na página de busca por máquinas **lava e seca** no site do **Carrefour Brasil**.

🔗 Página analisada:  
https://www.carrefour.com.br/busca/lava%20e%20seca


## 🧾 Objetivo

Coletar e armazenar dados de múltiplos produtos listados na página de busca, incluindo:
- Nome do Produto
- Preço
- Link para o Produto
- Marca 


## 🔧 Tecnologias utilizadas

- Python 3.12  
- `requests`  
- `BeautifulSoup` (bs4)  
- CSV (via módulo nativo `csv`)


## 📦 Como executar

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/webscraping-carrefour-lavaeseca.git
cd webscraping-carrefour-lavaeseca
```

### 2. Instalando as dependências
```bash
pip install -r requirements.txt
```

### 3. Execute o script de scraping
```bash
python scraper_carrefour.py
```

---

## 📄 Exemplo de saída (`produtos_lavaeseca.csv`)

| Nome do Produto                | Preço      | Link do Produto                              | Marca     |
|-------------------------------|------------|----------------------------------------------|-----------|
| Lava e Seca LG Smart 11kg...  | R$ 3.299,00| https://www.carrefour.com.br/xxxx            | LG        |




## 👩‍💻 Desenvolvido por

Isadora França  
Graduanda em Banco de dados • BI  

📌 Projeto desenvolvido como parte da avaliação da disciplina BI, ministrada pelo professor Heuber **"Construção de Aplicação Python para Extração de Preços de Produtos de E-commerce"**.
