# Single Link Clustering Project

Este projeto implementa o algoritmo Single Link para clustering de dados. 
A implementação está organizada em três arquivos principais na pasta `src`:

- `singlelink.py`: Implementação do algoritmo Single Link.
- `utils.py`: Funções que serão utilizadas pelo Single Link, além de leitura e escrita de arquivos.
- `main.py`: Script principal para rodar o Single Link e salvar os resultados.

## Instalação de Dependências

Para instalar as dependências necessárias, execute o comando abaixo:

```console
pip install -r requirements.txt
```

## Formato do Arquivo de Dados
O arquivo de dados deve estar no formato CSV padrão, com separação por vírgula. 
Os dados já devem estar tratados, sendo apenas numéricos, e decimais separados com ponto.

## Localização dos Arquivos de Dados
Coloque o arquivo CSV de entrada na pasta "data".

## Execução do Script
Para executar o script, navegue até a pasta raiz do projeto e execute o comando abaixo:

```console
python src/main.py nome_arquivo.csv
```

Caso a base de dados possua muitos registros a execução pode levar alguns minutos.

## Parâmetros
- filename (opcional): Nome do arquivo de entrada no formato CSV. Deve ser informado o nome completo com extensão.
Caso o filename não for informado o script será executado como exemplo didático com a base Iris.

## Arquivo de Saída
Os arquivos de saída serão gerados na pasta data/processed. 
Os nomes dos arquivos de saída serão:
- nome_arquivo_join.csv : contendo em cada linha os pares de clusters que foram agrupados em cada iteração.
    Os clusters novos gerados a partir das agregações vão recebendo um número incremental a partir da quantidade original de clusters. 
- nome_arquivo_clusters.txt : contendo em cada linha o conjunto de clusters por nível da hierarquia.
