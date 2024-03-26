import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Passo 7: Carregar os dados do arquivo Excel
df = pd.read_excel("cadastro_de_empregadores_01.xlsx")

# Passo 8: Identificar a quantidade de trabalhadores envolvidos em cada ação fiscal (RQ-01)
trabalhadores_por_acao = df.groupby('Ano da ação fiscal')['Trabalhadores envolvidos'].sum()

# Passo 9: Analisar a distribuição geográfica das ocorrências de trabalhos análogos à escravidão (RQ-02)
mapa = px.choropleth(df, 
                     locations='UF', 
                     locationmode='BR-states',
                     color='Trabalhadores envolvidos',
                     hover_name='UF',
                     title='Distribuição Geográfica das Ocorrências de Trabalhos Análogos à Escravidão')
mapa.update_geos(projection_type="mercator")

# Passo 10: Identificar o comportamento da prática ilegal ao longo do tempo (RQ-03)
linha_temporal = px.line(df, x='Ano da ação fiscal', y='Trabalhadores envolvidos', 
                         title='Comportamento Temporal das Ocorrências de Trabalhos Análogos à Escravidão')

# Passo 11: Identificar os setores econômicos com maior incidência de práticas ilegais (RQ-04)
setores_maiores_incidencias = df.groupby('CNAE')['Trabalhadores envolvidos'].sum().nlargest(10)

# Passo 12: Exibir as visualizações
plt.figure(figsize=(10, 5))
trabalhadores_por_acao.plot(kind='bar')
plt.title('Quantidade de Trabalhadores por Ação Fiscal')
plt.xlabel('Ano da Ação Fiscal')
plt.ylabel('Quantidade de Trabalhadores')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

mapa.show()

linha_temporal.show()

setores_maiores_incidencias.plot(kind='barh')
plt.title('Top 10 Setores com Maior Incidência de Práticas Ilegais')
plt.xlabel('Quantidade de Trabalhadores')
plt.ylabel('CNAE')
plt.tight_layout()
plt.show()
