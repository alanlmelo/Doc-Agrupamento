# SSWC Project

Este projeto implementa o algoritmo de validação Silhueta Simplificada (SSWC) para clustering de dados. 
A implementação está organizada em três arquivos principais na pasta `src`:

- `sswc.py`: Implementação do algoritmo SSWC.
- `utils.py`: Funções de suporte para execucação.
- `main.py`: Script principal que executa a clusterização no KMeans e no Single Link e depois o SSWC em cada Clusterização.

A pasta `models` contêm os algoritmos de clusterização que serão utilizados:
- `kmeans.py`: Implementação do Kmeans
- `singlelink.py`: Implementação do Single Link

## Instalação de Dependências

Para instalar as dependências necessárias, execute o comando abaixo:

```console
pip install -r requirements.txt
```

## Formato do Arquivo de Dados
O arquivo de dados deve estar no formato CSV padrão, com separação por vírgula.
Os dados já devem estar tratados, sendo apenas numéricos, e decimais separados com ponto.
Ou você também pode utilizar alguma das bases que já está disponível na pasta data.

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

## Saída
Ao final do processamento será impresso em tela o score de cada clusterização realizada, Kmeans e Single Link.
