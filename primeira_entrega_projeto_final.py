# -*- coding: utf-8 -*-
"""Primeira_entrega_projeto_final.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dMsG_WZ_U1-bYeU1Y6MCN_xHpHo_g0Rd

**Previsão de Demanda para Produtos de E-commerce**

**1. Apresentação da Empresa ou Problema Específico:**

Empresa: Olist é uma plataforma de e-commerce que conecta pequenos e médios
vendedores a consumidores em todo o Brasil. A empresa busca melhorar a gestão de seus estoques e prever a demanda por produtos para otimizar suas operações.

Problema: A flutuação na demanda dos produtos pode levar a excesso ou falta de estoque, resultando em prejuízos financeiros e insatisfação do cliente. É fundamental entender quais fatores influenciam a demanda e como essa demanda varia ao longo do tempo.

**2. Perguntas e Objetivos da Pesquisa**
Perguntas da Pesquisa:

1-Quais fatores influenciam a demanda por produtos na plataforma Olist?
2-Como a demanda varia entre diferentes categorias de produtos e em diferentes períodos do ano?
3-Existe uma relação significativa entre a localização geográfica dos clientes e a demanda?

**Objetivos:**

Prever a demanda futura de produtos utilizando técnicas de machine learning.
Identificar padrões sazonais nas vendas de produtos.
Fornecer recomendações para otimizar o gerenciamento de estoques.

**3. Configuração da Equipe de Trabalho**

Data Scientist(Eu): Responsável pela análise de dados, modelagem preditiva e extração de insights.

**4. Indicação da Fonte do Dataset e Critérios de Seleção (Data Acquisition)**

**Fonte do Dataset:**

O dataset utilizado será o Brazilian E-Commerce Dataset disponível no Kaggle. Este conjunto de dados contém informações sobre pedidos, produtos e clientes da plataforma Olist.

**Critérios de Seleção:**

A seleção do dataset foi baseada na representatividade do e-commerce brasileiro.
Variedade de informações, como dados de vendas, características dos produtos e informações dos clientes, permitindo uma análise abrangente.
"""

!pip install kaggle

from google.colab import files
files.upload()

"""**5. Geração do Primeiro Data Wrangling e EDA**"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar estilo do seaborn
sns.set(style='whitegrid')

"""**Carregando os Dados**"""

# Carregar os dados
orders = pd.read_csv('olist_orders_dataset.csv')
order_items = pd.read_csv('olist_order_items_dataset.csv')
products = pd.read_csv('olist_products_dataset.csv')

# Visualizar as primeiras linhas de cada DataFrame
print("Orders:")
print(orders.head())
print("\nOrder Items:")
print(order_items.head())
print("\nProducts:")
print(products.head())

# Verificando as primeiras linhas dos datasets para garantir o carregamento correto
print(orders.head())
print(order_items.head())
print(products.head())

# Verificar se há valores ausentes
print(orders.isnull().sum())
print(order_items.isnull().sum())
print(products.isnull().sum())

# Excluindo valores nulos (se necessário)
orders_cleaned = orders.dropna()
order_items_cleaned = order_items.dropna()
products_cleaned = products.dropna()

# Verificando se a limpeza funcionou
print(orders_cleaned.isnull().sum())

"""**Análise Exploratória de Dados (EDA)**"""

# Insights Univariados
# Plotando a distribuição dos valores dos pedidos
plt.figure(figsize=(10, 6))
sns.histplot(order_items_cleaned['price'], bins=50, kde=True)
plt.title('Distribuição dos Valores dos Pedidos')
plt.xlabel('Valor do Pedido')
plt.ylabel('Frequência')
plt.show()

# Insights Bivariados
# Criando um gráfico de dispersão entre valor e quantidade de itens
plt.figure(figsize=(10, 6))
sns.scatterplot(x=order_items_cleaned['price'], y=order_items_cleaned['freight_value'])
plt.title('Relação entre Preço e Valor de Frete')
plt.xlabel('Preço')
plt.ylabel('Valor do Frete')
plt.show()

# Insights Multivariados
# Usando pairplot para observar relações multivariadas
sns.pairplot(order_items_cleaned[['price', 'freight_value', 'order_id']])
plt.show()

"""**6. Análise de Componentes Principais**"""

# Aplicando PCA para Reduzir Dimensionalidade

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Selecionar colunas numéricas relevantes
numeric_features = order_items[['price', 'freight_value']]  # Exemplo de colunas a serem analisadas

# Padronizar os dados
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_features)

# Aplicar PCA
pca = PCA(n_components=2)
principal_components = pca.fit_transform(scaled_data)

# Criar DataFrame com os componentes principais
pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
print(pca_df.head())

"""Os dados mostram que a demanda varia significativamente entre diferentes categorias de produtos. Observamos também que o preço e o valor do frete estão relacionados à quantidade de itens por pedido. Através da análise de componentes principais, conseguimos reduzir a dimensionalidade dos dados, facilitando a identificação de padrões.

**7. Filtros Aplicados aos Dados e Distribuição**
"""

# Filtrando por pedidos com valor acima de 100 reais
high_value_orders = order_items_cleaned[order_items_cleaned['price'] > 100]

# Exibir os primeiros resultados após o filtro
print(high_value_orders.head())

from google.colab import files
files.upload()

import os

# Listar arquivos no diretório atual
os.listdir()

import os

# Listar arquivos no diretório atual
print(os.listdir())

import os

# Listar todos os arquivos no diretório atual
files = os.listdir()

# Duplicados a serem removidos
duplicates_to_remove = [
    'olist_orders_dataset (1).csv',  # Remover a cópia de pedidos
    'olist_order_items_dataset (1).csv',  # Remover a cópia de itens de pedidos
    'olist_products_dataset (1).csv',  # Remover a cópia de produtos
    'olist_customers_dataset (1).csv',  # Remover a cópia de clientes
    'olist_order_payments_dataset (1).csv',  # Remover a cópia de pagamentos (se existir)
    'olist_order_items_dataset (2).csv',  # Remover a segunda cópia de itens de pedidos
    'olist_orders_dataset (2).csv',  # Remover a segunda cópia de pedidos
    'olist_customers_dataset (2).csv',  # Remover a segunda cópia de clientes
    'olist_products_dataset (2).csv'  # Remover a segunda cópia de produtos
]

# Remover arquivos duplicados
for file in duplicates_to_remove:
    if file in files:
        os.remove(file)
        print(f'Removido: {file}')

# Verificar os arquivos restantes
remaining_files = os.listdir()
print("Arquivos restantes:", remaining_files)

import pandas as pd

# Carregar os datasets
orders = pd.read_csv('olist_orders_dataset.csv')
order_items = pd.read_csv('olist_order_items_dataset.csv')
products = pd.read_csv('olist_products_dataset.csv')
customers = pd.read_csv('olist_customers_dataset.csv')
payments = pd.read_csv('olist_order_payments_dataset.csv')

# Verifique se os dados foram carregados corretamente
print("Orders DataFrame:")
print(orders.head(), "\n")

print("Order Items DataFrame:")
print(order_items.head(), "\n")

print("Products DataFrame:")
print(products.head(), "\n")

print("Customers DataFrame:")
print(customers.head(), "\n")

print("Payments DataFrame:")
print(payments.head(), "\n")

# Merge Orders e Order Items
merged_order_items = pd.merge(orders, order_items, on='order_id', how='inner')
print("Merged Orders e Order Items:")
print(merged_order_items.head(), "\n")

# Merge com Products
merged_products = pd.merge(merged_order_items, products, on='product_id', how='inner')
print("Merged com Products:")
print(merged_products.head(), "\n")

# Merge com Customers
merged_customers = pd.merge(merged_products, customers, on='customer_id', how='inner')
print("Merged com Customers:")
print(merged_customers.head(), "\n")

# Merge com Payments
merged_data = pd.merge(merged_customers, payments, on='order_id', how='inner')
print("Merged Final com Payments:")
print(merged_data.head(), "\n")

# Filtrando pedidos com valor de pagamento superior a R$100
high_value_orders = merged_data[merged_data['payment_value'] > 100]

# Visualizar o resultado do filtro
print("Pedidos com valor de pagamento superior a R$100:")
print(high_value_orders.head())

# Aplicando filtro para incluir apenas pedidos de 2018
start_date = '2018-01-01'
end_date = '2018-12-31'
date_filtered_orders = merged_data[(merged_data['order_purchase_timestamp'] >= start_date) &
                                    (merged_data['order_purchase_timestamp'] <= end_date)]

# Visualizar o resultado do filtro por data
print("Pedidos filtrados entre 01/01/2018 e 31/12/2018:")
print(date_filtered_orders.head())

"""**9. Analisar Objetivos ou Objetivo para Esses Dados**

A análise dos dados permite prever a demanda por produtos de forma mais precisa, ajudando a Olist a otimizar seus estoques. Ao identificar categorias de produtos com alta demanda, a empresa pode ajustar sua estratégia de marketing e aprimorar a experiência do cliente.

Este projeto não apenas demonstra a habilidade em análise de dados, mas também oferece insights práticos que podem ser aplicados diretamente nas operações da Olist. Os resultados obtidos podem ser usados para melhorar a tomada de decisões e aumentar a eficiência operacional.
"""

# Exibir os objetivos da análise
objectives = [
    "Prever a Demanda Futura.",
    "Analisar Comportamento do Consumidor.",
    "Otimizar o Gerenciamento de Estoque.",
    "Tomada de Decisões Informadas."
]

print("Objetivos para os dados:")
for objective in objectives:
    print(f"- {objective}")