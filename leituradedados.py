#!pip install plotly numpy openpyxl nbformat ipykernel 
#1 importar a base de dados
import pandas as pd   
import plotly.express as px 
import numpy as np
tabela = pd.read_csv("cancelamentos_sample.csv")
#coluna intutil apaga , infomação vazia ou formatado 
#2 analisar a base de dados
    #o que eu tenho disponivel 
    #procaura os problemas da base de dados 
# #dropna tira celula vazias 
tabela = tabela.drop(columns=("CustomerID"))
#tira celula vazia 
tabela =  tabela.dropna()
#tira duplicados 
tabela = tabela.drop_duplicates()
#3 analisa motivo do cancelamento
#cria grafico e sempre em duas etapas
    #cria o grafico
for coluna in tabela :
    grafico = px.histogram(tabela,x=coluna ,color="cancelou",text_auto=True,)
    #depois exibe 
    grafico.show()