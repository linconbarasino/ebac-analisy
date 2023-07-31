import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados do arquivo CSV em um DataFrame
df = pd.read_csv('gasolina.csv')

# Criar o gráfico de linha
plt.figure(figsize=(10, 6))
sns.lineplot(x='dia', y='venda', data=df)
plt.title('Preço da Gasolina ao Longo dos Dias', fontsize=16)
plt.xlabel('Dia', fontsize=14)
plt.ylabel('Preço da Gasolina', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True)

# Salvar o gráfico como imagem
plt.savefig('gasolina.png')

# Exibir o gráfico
plt.show()
