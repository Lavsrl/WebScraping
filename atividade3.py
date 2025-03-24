import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Acesse o site Buscapé ou Zoom (ou outro site de sua escolha
# que exiba preços de smartphones).
# Acesso ao site do Zoom:

url = "https://www.zoom.com.br/celular"

headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

# 2. Identifique a estrutura do HTML para encontrar os nomes dos produtos e seus preços.

    produtos = soup.find_all("h2", {"data-testid": "product-card::name"})  # Ajuste a classe conforme inspeção
    precos = soup.find_all("p", {"data-testid": "product-card::price"})

    lista_produtos = []

# 3. Extraia pelo menos 5 modelos de smartphones e seus preços.
    for i in range(min(5, len(produtos))):
        nome = produtos[i].text.strip()
        preco = precos[i].text.strip()
        lista_produtos.append([nome, preco])

# 4. Exiba os resultados formatados no terminal.
    print("\n Lista de Smartphones e Preços:\n")
    for produto in lista_produtos:
        print(f"{produto[0]} - Preço: {produto[1]}")

# 5. Salve os preços em um arquivo CSV.
    df = pd.DataFrame(lista_produtos, columns=["Produto", "Preço"])
    df.to_csv("precos_smartphones.csv", index=False, encoding="utf-8")

    print("\n Dados salvos no arquivo 'precos_smartphones.csv'.")

else:
    print("Erro:", response.status_code)
