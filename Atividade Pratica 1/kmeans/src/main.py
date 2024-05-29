#External imports
import argparse

#Internal imports
from kmeans import KMeans
from utils import load_file, save_data

def main():
    parser = argparse.ArgumentParser(description='KMeans clustering')
    parser.add_argument('filename', type=str, help='Input CSV file', nargs='?', default='iris.csv')
    parser.add_argument('--n_clusters', type=int, help='Number of clusters', default=3)
    parser.add_argument('--max_iter', type=int, help='Maximum number of iterations', default=100)
    parser.add_argument('--random_state', type=int, help='Random state for initialization', default=None)
    
    args = parser.parse_args()

    data = load_file(args.filename)
    if data is None:
        return
    
    data_values = data.values
    
    model = KMeans(n_clusters=args.n_clusters, max_iter=args.max_iter, random_state=args.random_state)
    model.fit(data_values)

    print("filename:", args.filename)
    print("n_clusters:", args.n_clusters)
    print("max_iter:", args.max_iter)
    print("random_state:", args.random_state)
    print("Iterações Realizadas:", model.n_itered_)
    print("Centroides:\n", model.centroids_)
    
    save_data(data, model.labels_, args.filename)

if __name__ == '__main__':
    main()
