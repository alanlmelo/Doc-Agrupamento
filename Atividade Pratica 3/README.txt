Atividade Pratica 1: Implementação do Algoritmo Single Link

Para executar o algoritmo siga os seguintes passos.

1) Copie a pasta singlelink para um ambiente com Python configurado

2) Via console, navegue até a pasta do projeto e instale as dependências com o comando: 

pip install -r requirements.txt

3) Copie para a pasta "/singlelink/data" o arquivo com os dados a serem processados.
O arquivo de dados deve estar no formato CSV padrão, com separação por vírgula.

4) Para executar o script, via console navegue até a pasta raiz do projeto e execute o comando abaixo:

python src/main.py nome_arquivo.csv

Orientação sobre os Parâmetros
- filename (opcional): Nome do arquivo de entrada no formato CSV. Deve ser informado o nome completo com extensão.

Caso o filename não for informado o script será executado como exemplo didático com a base Iris.

5) Os arquivos de saída serão gerados na pasta data/processed. 
Os nomes dos arquivos de saída serão:
- nome_arquivo_join.csv : contendo em cada linha os pares de clusters que foram agrupados em cada iteração.
    Os clusters novos gerados a partir das agregações vão recebendo um número incremental a partir da quantidade original de clusters. 
- nome_arquivo_clusters.txt : contendo em cada linha o conjunto de clusters por nível da hierarquia.
