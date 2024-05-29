#External imports
import numpy as np

#Internal imports
from utils import shorter_dist 

class KMeans:

    def __init__(self, n_clusters, max_iter, random_state=None):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.random_state = random_state
        self.centroids_ = None
        self.labels_ = None
        self.n_itered_ = 0

    #Excuta o algoritmo
    def fit(self, X):

        if self.random_state:
            np.random.seed(self.random_state)        

        #Quantidade de elementos
        k = X.shape[0]

        #Inicializando os centróides
        indexes = np.random.choice(k, size=self.n_clusters, replace=False)
        centroids = X[indexes]
        self.centroids_ = centroids.copy()

        #Clusters iniciais
        clusters = np.array([shorter_dist(e, centroids) for e in X])

        #Realiza as iterações do Algorítmo até ite_limit
        for _ in range(self.max_iter):

            #Recalcula os centróides
            for c in range(self.n_clusters):
                #Filtra os elementos de X do Cluster c
                filtered_cluster = X[(clusters == c)]
                #Calcula o Centróide do cluster
                centroids[c] = np.mean(filtered_cluster, axis=0)

            # Verifica convergência
            if np.all(centroids == self.centroids_):
                break

            #Redefine o grupo dos elementos a partir dos novos centróides
            clusters = np.array([shorter_dist(e, centroids) for e in X])
            self.centroids_ = centroids.copy()
            self.n_itered_ += 1

        self.labels_ = clusters
