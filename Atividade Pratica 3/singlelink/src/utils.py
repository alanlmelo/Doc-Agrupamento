#External imports
import os
import csv
import pandas as pd

#Retorna a Distância Euclidiana entre 2 pontos
def euclidian_dist(p1, p2):
  # Calcula a diferença entre as coordenadas de cada dimensão
  squares_diffs = [(x2 - x1)**2 for x1, x2 in zip(p1, p2)]

  # Calcula a soma dos quadrados das diferenças
  sum_squares = sum(squares_diffs)

  # Calcula a raiz quadrada da soma dos quadrados
  distance = sum_squares**0.5

  return distance

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

#Gera o Arquivo de Saída indicando as agregações em cada iteração
def save_data_join(linkage, filename):
  script_dir = os.path.dirname(os.path.abspath(__file__))
  processed_dir = os.path.join(script_dir, '..', 'data', 'processed')
  os.makedirs(processed_dir, exist_ok=True)

  # Caminho completo para o arquivo de saída    
  base_name = os.path.splitext(filename)[0]
  output_filename = f"{base_name}_join.csv"
  output_file_path = os.path.join(processed_dir, output_filename)

  with open(output_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['nivel', 'cluster_1', 'cluster_2'])

    for i, (c1, c2, dist, size) in enumerate(linkage):
      # O índice de cada cluster é ajustado para ser baseado em 1 para facilitar a referência
      writer.writerow([i + 1, int(c1 + 1), int(c2 + 1)])

  print(f"Arquivo de saída 1 gerado em: {output_file_path}")

#Gera o Arquivo de Saída indicando os clusters em cada nivel da hierarquia
def save_data_clusters(k, linkage, filename):
  script_dir = os.path.dirname(os.path.abspath(__file__))
  processed_dir = os.path.join(script_dir, '..', 'data', 'processed')
  os.makedirs(processed_dir, exist_ok=True)

  # Caminho completo para o arquivo de saída    
  base_name = os.path.splitext(filename)[0]
  output_filename = f"{base_name}_clusters.txt"
  output_file_path = os.path.join(processed_dir, output_filename)

  with open(output_file_path, 'w', newline='') as file:
    writer = csv.writer(file)

    # Inicializando os grupos com cada elemento em seu próprio grupo
    clusters = {i: [i] for i in range(k)}

    # Processando cada união e atualizando os grupos
    for i, (c1, c2, dist, size) in enumerate(linkage):
      # Unindo os grupos
      clusters[k + i] = clusters.pop(int(c1)) + clusters.pop(int(c2))
      # Imprimindo o estado atual dos grupos após cada união
      writer.writerow([format_clusters(clusters)])

  print(f"Arquivo de saída 2 gerado em: {output_file_path}")

# Função para formatar um cluster
def format_clusters(clusters):
  return ', '.join(['{' + ', '.join(map(str, sorted(cluster))) + '}' for cluster in clusters.values()])
