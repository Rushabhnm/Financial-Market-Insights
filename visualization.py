import pandas as pd
import matplotlib.pyplot as plt

def load_clustered_data(input_file):
    """Loads clustered data from CSV."""
    data = pd.read_csv(input_file, index_col='Date', parse_dates=True)
    return data

def visualize_clusters(clustered_data):
    """Generates visualizations of clustered data."""
    plt.figure(figsize=(10, 6))
    for cluster_id in clustered_data['Cluster'].unique():
        cluster_data = clustered_data[clustered_data['Cluster'] == cluster_id]
        plt.plot(cluster_data.index, cluster_data['Close'], label=f'Cluster {cluster_id}')

    plt.title('Stock Price Trends by Cluster')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Example usage
    input_file = 'data/clustered_data.csv'

    # Load clustered data
    clustered_data = load_clustered_data(input_file)

    # Visualize clusters
    visualize_clusters(clustered_data)

    print("Visualization completed.")
