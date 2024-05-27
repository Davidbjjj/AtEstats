import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
import seaborn as sns

# Dados fornecidos
nota_teste = [
    7.5, 8, 9, 7, 7.5, 6, 10, 7, 8, 8.5, 10, 9, 3, 7, 2, 4, 5, 3, 6, 5,
    4, 2.5, 2, 2, 1.5, 5, 4, 8, 7, 8, 10, 7, 9, 7, 7.5, 8, 6, 8, 8, 8,
    7, 9, 7, 9, 7, 8, 9, 7, 8, 7.5
]
tipoesc = [
    'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv',
    'priv', 'priv', 'priv', 'priv', 'pub', 'pub', 'pub', 'pub', 'pub', 'pub',
    'pub', 'pub', 'pub', 'pub', 'pub', 'pub', 'pub', 'priv', 'priv', 'priv',
    'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv', 'priv',
    'priv', 'priv', 'priv', 'pub', 'pub', 'pub', 'pub', 'priv', 'priv', 'priv', 'pub'
]

# Criar DataFrame
df = pd.DataFrame({
    'TipoEsc': tipoesc,
    'Nota_Teste': nota_teste
})

# Separar os dados por tipo de escola
notas_priv = df[df['TipoEsc'] == 'priv']['Nota_Teste']
notas_pub = df[df['TipoEsc'] == 'pub']['Nota_Teste']

# Realizar o teste t
t_stat, p_value = ttest_ind(notas_priv, notas_pub)

# Exibir os resultados do teste t
print(f'Estatística t: {t_stat:.3f}')
print(f'Valor p: {p_value:.3f}')

# Plotar a distribuição das notas
plt.figure(figsize=(14, 6))

# Subplot 1: Distribuição das notas
plt.subplot(1, 2, 1)
sns.histplot(notas_priv, kde=True, color='blue', label='Privadas', bins=10)
sns.histplot(notas_pub, kde=True, color='orange', label='Públicas', bins=10)
plt.title('Distribuição das Notas por Tipo de Escola')
plt.xlabel('Nota')
plt.ylabel('Frequência')
plt.legend()

# Subplot 2: Médias das notas
plt.subplot(1, 2, 2)
mean_priv = notas_priv.mean()
mean_pub = notas_pub.mean()
plt.bar(['Privadas', 'Públicas'], [mean_priv, mean_pub], color=['blue', 'orange'])
plt.title('Média das Notas por Tipo de Escola')
plt.ylabel('Média da Nota')

# Exibir os gráficos
plt.tight_layout()
plt.show()
