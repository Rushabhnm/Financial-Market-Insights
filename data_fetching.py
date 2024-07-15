import pandas as pd
import yfinance as yf

def fetch_stock_data(tickers, start_date, end_date):
    """Fetches historical stock data from Yahoo Finance."""
    data = yf.download(tickers, start=start_date, end=end_date)
    return data

def preprocess_data(stock_data):
    """Preprocesses the fetched stock data."""
    # Example preprocessing steps (you can customize as needed)
    stock_data = stock_data['Close']  # Use only the 'Close' prices for simplicity
    stock_data.fillna(method='ffill', inplace=True)  # Fill missing values using forward fill
    return stock_data

def save_processed_data(processed_data, output_file):
    """Saves processed data to a CSV file."""
    processed_data.to_csv(output_file, index_label='Date')

if __name__ == "__main__":
    # Example usage
    tickers = ['AAPL', 'GOOGL', 'MSFT']  # Example list of tickers
    start_date = '2023-01-01'
    end_date = '2023-12-31'

    # Fetch data
    stock_data = fetch_stock_data(tickers, start_date, end_date)

    # Preprocess data
    processed_data = preprocess_data(stock_data)

    # Save processed data
    output_file = 'data/processed_data.csv'
    save_processed_data(processed_data, output_file)

    print("Data fetching and preprocessing completed.")
