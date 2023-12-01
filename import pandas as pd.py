import pandas as pd

# Passo a passo de solução 

# Abrir os 6 arquivos em Excel
lista_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho"]
tabela_vendas = pd.read_excel ("janeiro.xlsx")
Print (tabela_vendas)

#Para cada arquivo:
#Verficar se algum valor na coluna Venda é maior que 55k
#Se for maior que 55k -> Enviar um SMS com o nome, mês e vendas do mesmo

#Instalar: Pandas, openpyxl e Twilio