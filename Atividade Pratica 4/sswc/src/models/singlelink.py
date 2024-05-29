#External imports
import numpy as np

#Internal imports
from utils import euclidian_dist 

class SingleLink:

    def __init__(self):
        self.linkage_ = None
        self.n_itered_ = 0

    def fit(self, X):

        k = X.shape[0] #Quantidade de elementos
        num_clusters = k #Quantidade de clusters iniciais
        last_cluster = k - 1 #Indice do último cluster

        #Gerando a matriz de distâncias
        m_dist = np.zeros((k, k))

        for i in range(k):
            for j in range(i+1, k):
                m_dist[i][j] = m_dist[j][i] = euclidian_dist(X[i], X[j])

        #Gera uma lista de controle dos Clusters, com o tamanho do Cluster e o cluster de destino dele
        #Inicialmente considera cada elemento um cluster individual, tamanho 1 e cluster de destino None
        clusters = np.full((k, 2), fill_value=[1, None], dtype=object)

        linkage = []

        while num_clusters > 1:

            dist_min = np.inf
            min_i = None
            min_j = None

            #Busca a menor distância na matriz
            for i in range(last_cluster+1):
                if clusters[i][1] is None:
                    for j in range(i+1, last_cluster+1):
                        if clusters[j][1] is None and m_dist[i][j] < dist_min:
                            dist_min = m_dist[i][j]
                            min_i = i
                            min_j = j

            num_clusters -= 1
            last_cluster += 1

            clusters = np.vstack([clusters, [clusters[min_i][0] + clusters[min_j][0], None]]) #Adiciona o novo cluster na lista
            clusters[min_i][1] = clusters[min_j][1] = last_cluster #Adiciona o destino dos 2 clusters agregados

            new_cluster_dist = np.minimum(m_dist[min_i], m_dist[min_j]) #Gera as distancias do novo cluster a partir dos agregados

            m_dist = np.hstack((m_dist, new_cluster_dist[:, None])) #Adiciona uma nova coluna na matriz de distância referente ao novo cluster

            new_cluster_dist = np.append(new_cluster_dist, 0) #Adiciona a posição que ficará na diagonal
            m_dist = np.vstack((m_dist, new_cluster_dist)) #Adiciona a linha referente ao novo cluster

            linkage.append([min_i, min_j, dist_min, clusters[last_cluster][0]])

        self.linkage_ = linkage
