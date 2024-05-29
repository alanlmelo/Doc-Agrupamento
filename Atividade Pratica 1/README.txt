Atividade Pratica 1: Implementação do Algoritmo Kmeans

Para executar o algoritmo siga os seguintes passos.

1) Copie a pasta kmeans para um ambiente com Python configurado

2) Via console, navegue até a pasta do projeto e instale as dependências com o comando: 

pip install -r requirements.txt

3) Copie para a pasta "/kmeans/data" o arquivo com os dados a serem processados.
O arquivo de dados deve estar no formato CSV padrão, com separação por vírgula.

4) Para executar o script, via console navegue até a pasta raiz do projeto e execute o comando abaixo:

python src/main.py nome_arquivo.csv --n_clusters 3 --max_iter 100 --random_state 42

Orientação sobre os Parâmetros
- filename (opcional): Nome do arquivo de entrada no formato CSV. Deve ser informado o nome completo com extensão.
- --n_clusters (opcional): Número de clusters. Padrão: 3
- --max_iter (opcional): Número máximo de iterações. Padrão: 100
- --random_state (opcional): Estado aleatório para inicialização. Padrão: None

Todos os parâmetros são opcionais e caso não forem informados o script será executado como exemplo didático com a base Iris e os demais valores padrão.

5) Será gerado um arquivo de saída na pasta data/processed.
O arquivo irá conter os dados originais acrescidos de uma coluna label que indica o cluster ao qual cada ponto foi atribuído. 
O nome do arquivo de saída será o mesmo nome do arquivo de entrada, com o sufixo _clustered e a extensão .csv, Ex: nome_original_processed.csv
