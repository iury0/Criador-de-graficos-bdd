import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configurações globais para melhor visualização
plt.style.use('default')  # Usando o estilo padrão do matplotlib
sns.set_theme()  # Configurando o tema do seaborn
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

def carregar_dados():
    """Carrega os dados do arquivo CSV"""
    return pd.read_csv('cancelamentos_sample.csv')

def criar_graficos(df):
    """Função principal para criar os gráficos"""
    # Aqui você pode adicionar todas as funções de criação de gráficos
    pass

def main():
    # Carrega os dados
    df = carregar_dados()
    
    # Cria os gráficos
    criar_graficos(df)
    
    # Mostra todos os gráficos
    plt.show()

if __name__ == "__main__":
    main()