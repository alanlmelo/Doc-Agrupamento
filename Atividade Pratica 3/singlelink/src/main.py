#External imports
import time
import argparse

#Internal imports
from singlelink import SingleLink
from utils import load_file, save_data_join, save_data_clusters

def main():
    parser = argparse.ArgumentParser(description='Single Link clustering')
    parser.add_argument('filename', type=str, help='Input CSV file', nargs='?', default='iris.csv')
    args = parser.parse_args()

    data = load_file(args.filename)
    if data is None:
        return
    
    data_values = data.values
    
    start_time = time.perf_counter()
    
    model = SingleLink()
    model.fit(X=data_values)
    
    end_time = time.perf_counter()    
    execution_time = end_time - start_time

    print(f"Execution time : {execution_time:.4f} seconds")
    print("filename:", args.filename)

    save_data_join(linkage=model.linkage_, filename=args.filename)
    save_data_clusters(k=data_values.shape[0], linkage=model.linkage_, filename=args.filename)

if __name__ == '__main__':
    main()
