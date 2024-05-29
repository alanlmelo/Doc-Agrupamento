# KMeans Clustering Project

Este projeto implementa o algoritmo KMeans para clustering de dados. 
A implementação está organizada em três arquivos principais na pasta `src`:

- `kmeans.py`: Implementação do algoritmo KMeans.
- `utils.py`: Funções que serão utilizadas pelo KMeans, além de leitura e escrita de arquivos.
- `main.py`: Script principal para rodar o KMeans e salvar os resultados.

## Instalação de Dependências

Para instalar as dependências necessárias, execute o comando abaixo:

```console
pip install -r requirements.txt
```

## Formato do Arquivo de Dados
O arquivo de dados deve estar no formato CSV padrão, com separação por vírgula.

## Localização dos Arquivos de Dados
Coloque o arquivo CSV de entrada na pasta "data".

## Execução do Script
Para executar o script, navegue até a pasta raiz do projeto e execute o comando abaixo:

```console
python src/main.py nome_arquivo.csv --n_clusters 3 --max_iter 100 --random_state 42
```

## Parâmetros
- filename (opcional): Nome do arquivo de entrada no formato CSV. Deve ser informado o nome completo com extensão.
- --n_clusters (opcional): Número de clusters. Padrão: 3
- --max_iter (opcional): Número máximo de iterações. Padrão: 100
- --random_state (opcional): Estado aleatório para inicialização. Padrão: None

Todos os parâmetros são opcionais e caso não forem informados o script será executado como exemplo didático com a base Iris e os demais valores padrão.

## Arquivo de Saída
Um arquivo de saída será gerado na pasta data/processed, contendo os dados originais acrescidos de uma coluna label que indica o cluster ao qual cada ponto foi atribuído. 
O nome do arquivo de saída será o mesmo nome do arquivo de entrada, com o sufixo _clustered e a extensão .csv.