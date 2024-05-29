#External imports
import time
import argparse

#Internal imports
from models.kmeans import KMeans
from models.singlelink import SingleLink
from sswc import SSWC
from utils import load_file, extract_clusters

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
    
    start_time_k = time.perf_counter()
    model_kmeans = KMeans(n_clusters=args.n_clusters, max_iter=args.max_iter, random_state=args.random_state)
    model_kmeans.fit(data_values)
    end_time_k = time.perf_counter()

    start_time_sl = time.perf_counter()
    model_singlelink = SingleLink()
    model_singlelink.fit(X=data_values)
    sl_labels = extract_clusters(linkage=model_singlelink.linkage_, k=args.n_clusters, n=data_values.shape[0])
    end_time_sl = time.perf_counter()

    start_time_sswc = time.perf_counter()
    sswc_kmeans = SSWC(X=data_values, labels=model_kmeans.labels_, k=args.n_clusters, centroids=model_kmeans.centroids_)
    sswc_singlelink = SSWC(X=data_values, labels=sl_labels, k=args.n_clusters)
    end_time_sswc = time.perf_counter()

    print(f"Execution time kmeans: {end_time_k - start_time_k:.4f} seconds")
    print(f"Execution time Single Link: {end_time_sl - start_time_sl:.4f} seconds")    
    print(f"Execution time SSWC (2x): {end_time_sswc - start_time_sswc:.4f} seconds")

    print("filename:", args.filename)
    print("n_clusters:", args.n_clusters)
    print("max_iter:", args.max_iter)
    print("random_state:", args.random_state)  
    print("\nSSWC Kmeans:", sswc_kmeans)
    print("SSWC Single Link:", sswc_singlelink)

if __name__ == '__main__':
    main()
