#External imports
import numpy as np

#Internal imports
from utils import euclidian_dist 

def SSWC(X, labels, k, centroids=None):

    if centroids is None:
        centroids = np.array([np.mean(X[labels == i], axis=0) for i in range(k)])

    #Calcula as distâncias de cada ponto aos centróides
    dist_to_centroids = np.array([[euclidian_dist(xi, cj) for cj in centroids] for xi in X])

    #Identifica a distância calculada de cada ponto ao centróide do próprio Cluster
    A = np.array([dist_to_centroids[i, label] for i, label in enumerate(labels)])

    #Identifica a distância calculada de cada ponto ao centróide do Cluster mais pŕoximo
    B = np.array([np.min([dist_to_centroids[i, c] for c in range(len(centroids)) if c != label]) for i, label in enumerate(labels)])

    #Calcula a Silhueta de cada ponto
    S = (B - A) / np.maximum(A, B)

    #Calcula a Silhueta Final
    score = np.mean(S)

    return score
