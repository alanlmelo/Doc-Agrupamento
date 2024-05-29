import os
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

#Gera o Arquivo de Saída
def save_data(data, labels, filename):
  script_dir = os.path.dirname(os.path.abspath(__file__))
  processed_dir = os.path.join(script_dir, '..', 'data', 'processed')
  os.makedirs(processed_dir, exist_ok=True)

  # Adicionar os labels ao DataFrame    
  data['label'] = labels

  # Caminho completo para o arquivo de saída    
  base_name = os.path.splitext(filename)[0]
  output_filename = f"{base_name}_clustered.csv"
  output_file_path = os.path.join(processed_dir, output_filename)

  # Salvar o DataFrame como CSV
  data.to_csv(output_file_path, index=False)
  print(f"Arquivo de saída salvo em: {output_file_path}")
