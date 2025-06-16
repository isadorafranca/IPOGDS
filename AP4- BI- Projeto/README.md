# Web Scraping Carrefour - Lava e Seca

Este projeto consiste em uma aplicação Python que realiza **web scraping** na página de busca por máquinas **lava e seca** no site do **Carrefour Brasil**.

🔗 Página analisada:  
https://www.carrefour.com.br/busca/lava%20e%20seca

---

## 🧾 Objetivo

Coletar e armazenar dados de múltiplos produtos listados na página de busca, incluindo:
- Nome do Produto
- Preço
- Link para o Produto
- Marca (se disponível)

Esses dados são salvos em um arquivo CSV para fins de análise e comparação de preços.

---

## 🔧 Tecnologias utilizadas

- Python 3.x  
- `requests`  
- `BeautifulSoup` (bs4)  
- CSV (via módulo nativo `csv`)

---

## 📦 Como executar

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/webscraping-carrefour-lavaeseca.git
cd webscraping-carrefour-lavaeseca
```

### 2. Instale as dependências
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

---

## ⚠️ Observações

- O conteúdo é carregado diretamente no HTML, o que facilita o uso de BeautifulSoup.
- Não é necessário uso de `Selenium`.
- Em caso de alterações na estrutura da página pelo Carrefour, pode ser necessário ajustar os seletores HTML no código.

---

## ✅ Ética e boas práticas

- A coleta de dados foi realizada **apenas em páginas públicas**, sem login.
- O volume de requisições foi controlado, evitando sobrecarga.
- Uso exclusivamente educacional, respeitando os Termos de Uso do site.

---

## 👩‍💻 Desenvolvido por

Isadora Pereira  
Graduanda em Ciência de Dados • Bióloga • Educadora  
[GitHub](https://github.com/seu-usuario) | [LinkedIn](https://linkedin.com/in/seu-perfil)

---

📌 Projeto desenvolvido como parte da atividade **"Construção de Aplicação Python para Extração de Preços de Produtos de E-commerce"**.
