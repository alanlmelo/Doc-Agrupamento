Atividade Pratica 4: Implementação do Algoritmo de Validação Silhueta Simplificada (SSWC) para clustering de dados. 

Para executar o algoritmo siga os seguintes passos.

1) Copie a pasta sswc para um ambiente com Python configurado

2) Via console, navegue até a pasta do projeto e instale as dependências com o comando: 

pip install -r requirements.txt

3) Copie para a pasta "/sswc/data" o arquivo com os dados a serem processados.
O arquivo de dados deve estar no formato CSV padrão, com separação por vírgula.
Ou você também pode utilizar alguma das bases que já está disponível na pasta data.

4) Para executar o script, via console navegue até a pasta raiz do projeto e execute o comando abaixo:

python src/main.py nome_arquivo.csv --n_clusters 3 --max_iter 100 --random_state 42

Orientação sobre os Parâmetros
- filename (opcional): Nome do arquivo de entrada no formato CSV. Deve ser informado o nome completo com extensão.
- --n_clusters (opcional): Número de clusters. Padrão: 3
- --max_iter (opcional): Número máximo de iterações. Padrão: 100
- --random_state (opcional): Estado aleatório para inicialização. Padrão: None

Todos os parâmetros são opcionais e caso não forem informados o script será executado como exemplo didático com a base Iris e os demais valores padrão.

5) Ao final do processamento será impresso em tela o score de cada clusterização realizada, Kmeans e Single Link.
