# pd = pandas
# dataframe = tabela
# dataframe = pd.DataFrame()

# Criando um Dataframe a partir de um dicionário:
import pandas as pd

venda = {
    "data": ['15/02/2021', '16/02/2021'],
    "valor":[500,300],
    "produto": ["feijao","arroz"],
    "qtd" : [50,70],
}
print(venda)

vendas_df = pd.DataFrame(venda)
print(vendas_df)


# Visualização de dados:
# display ()
# print ()

print(vendas_df)

# importando arquivos e base de dados 
vendas_df = pd.read_excel("Vendas.xlsx")