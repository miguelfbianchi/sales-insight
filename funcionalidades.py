# importação de bibliotecas
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import matplotlib.pyplot as plt
import seaborn as sns
import os
import json
import re

# RF01 – Criar ou Carregar o Dataset de Vendas
"""Gera um dataset sintético de vendas com dados intencionalmente sujos."""

def gerar_dataset_vendas(n_registros=200, seed=42):

    random.seed(seed)       # inicialização do gerador aleatório interno da biblioteca random
    np.random.seed(seed)    # faz o mesmo para o Numpy

    produtos = ["Notebook", "Smartphone", "Tablet", "Monitor", "Teclado", "Mouse", "Headset"]
    categorias = {"Notebook": "Computadores", "Smartphone": "Celulares", "Tablet": "Celulares",
                "Monitor": "Computadores", "Teclado": "Periféricos", "Mouse": "Periféricos",
                "Headset": "Periféricos"}
    regioes = ["Sudeste", "Sul", "Nordeste", "Centro-Oeste", "Norte"]
    clientes = [f"Cliente_{i:03d}" for i in range(1, 51)]   # geração de ids de 50 clientes com formato padronizado

    data_inicio = datetime(2024, 1, 1)
    dados = []

    for i in range(n_registros):
        produto = random.choice(produtos)       # escolhe um produto aleatório da lista
        quantidade = random.randint(1, 10)      # escolhe uma quantidade inteira entre 1 e 10
        preco_base = {"Notebook": 3500, "Smartphone": 2200, "Tablet": 1800,
                        "Monitor": 1200, "Teclado": 250, "Mouse": 120,
                        "Headset": 350}[produto] # escolhe o preço base buscando no dicionário com a chave gerada em produto
        
        preco = round(preco_base * random.uniform(0.85, 1.15), 2)
        #estabelece um preço que varia 15% a mais ou a menos aleatoriamente a partir do preço base

        data = data_inicio + timedelta(days=random.randint(0, 364))     # gera uma data aleatória no universo de um ano

        # Inserindo dados intencionalmente sujos para limpeza
        if random.random() < 0.05:
            quantidade = None # valor nulo de quantidade para aprox. 5% das entradas
        if random.random() < 0.04:
            preco = None # valor nulo de preço para aprox. 4% das entradas
        if random.random() < 0.03:
            produto = " " + produto # espaço extra (string suja) para aprox. 3% das entradas de nomes de produtos

        # adiciona um dicionário com os dados da vendaà lista geral
        dados.append({
            "id_venda": i + 1, # acrescenta 1 pois a contagem do range inicia em zero
            "data_venda": data.strftime("%Y-%m-%d") if random.random() > 0.02 else "DATA INVÁLIDA",
            # atribui datas inválidas a ~2% das entradas
            "cliente": random.choice(clientes), #cliente aleatorio
            "produto": produto,
            "categoria": categorias.get(produto.strip(), "Outros"),
            "regiao": random.choice(regioes),
            "quantidade": quantidade,
            "preco_unitario": preco
                    })

    return pd.DataFrame(dados)


