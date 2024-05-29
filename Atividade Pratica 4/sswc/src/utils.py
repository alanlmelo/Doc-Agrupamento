#External imports
import os
import pandas as pd
import numpy as np

#Retorna a Distância Euclidiana entre 2 pontos
def euclidian_dist(p1, p2):
  # Calcula a diferença entre as coordenadas de cada dimensão
  squares_diffs = [(x2 - x1)**2 for x1, x2 in zip(p1, p2)]

  # Calcula a soma dos quadrados das diferenças
  sum_squares = sum(squares_diffs)

  # Calcula a raiz quadrada da soma dos quadrados
  distance = sum_squares**0.5

  return distance

#Retorna o índice do Centróide mais próximo do Elemento usando a dist. Euclidiana
def shorter_dist(e, C):
  # Gera um array com a distãncia euclediana do elemento x com cada centróide
  distances = [euclidian_dist(e, c) for c in C]

  # Pega o índice da menor distancia calculada
  index = distances.index(min(distances))

  return index

#Lê o Arquivo de Entrada
def load_file(filename):
  script_dir = os.path.dirname(os.path.abspath(__file__))
  data_dir = os.path.join(script_dir, '..', 'data')
  file_path = os.path.join(data_dir, filename)

  try:
    data = pd.read_csv(file_path)
    return data
  except FileNotFoundError:
    print(f"Arquivo {filename} não encontrado no diretório {data_dir}")
    return None
  except pd.errors.EmptyDataError:
    print(f"Arquivo {filename} está vazio")
    return None
  except pd.errors.ParserError:
    print(f"Erro ao analisar o arquivo {filename}")
    return None

#Extrai os labels dos Clusters a partir da matriz linkage
def extract_clusters(linkage, k, n):
    # Inicializar os clusters: cada ponto começa em seu próprio cluster
    clusters = np.arange(n)
    
    # Iterar sobre a matriz linkage
    for i, (c1, c2, dist, size) in enumerate(linkage):
      c1, c2 = int(c1), int(c2)
      # Atualizar os clusters, mesclando c1 e c2
      clusters[clusters == c1] = n + i
      clusters[clusters == c2] = n + i

      # Checar o número de clusters únicos encontrados
      unique_clusters = np.unique(clusters)
      if len(unique_clusters) == k:
        break

    labels = np.zeros_like(clusters)
    for index, unique in enumerate(unique_clusters):
      labels[clusters == unique] = index

    return labels
