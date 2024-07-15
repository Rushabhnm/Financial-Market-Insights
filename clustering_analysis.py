import pandas as pd
from sklearn.cluster import KMeans

def load_data(input_file):
    """Loads processed data from CSV."""
    data = pd.read_csv(input_file, index_col='Date', parse_dates=True)
    return data

def apply_kmeans_clustering(data, num_clusters):
    """Applies K-means clustering to the data."""
    kmeans = KMeans(n_clusters=num_clusters, random_state=0)
    data['Cluster'] = kmeans.fit_predict(data.values.reshape(-1, 1))
    return data

def save_clustered_data(clustered_data, output_file):
    """Saves clustered data to a CSV file."""
    clustered_data.to_csv(output_file, index_label='Date')

if __name__ == "__main__":
    # Example usage
    input_file = 'data/processed_data.csv'
    output_file = 'data/clustered_data.csv'
    num_clusters = 3  # Example number of clusters

    # Load data
    data = load_data(input_file)

    # Apply K-means clustering
    clustered_data = apply_kmeans_clustering(data, num_clusters)

    # Save clustered data
    save_clustered_data(clustered_data, output_file)

    print("Clustering analysis completed.")
