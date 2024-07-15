# Real-Time Stock Data Analysis of Fortune 500 Companies

## Project Overview

This project focuses on procuring real-time stock data for Fortune 500 companies from Yahoo Finance and analyzing common trends in their stock price movements using unsupervised machine learning techniques. The primary goal is to enable informed data-driven decision-making for portfolio diversification, risk management, and sector analysis by categorizing companies based on their daily stock market fluctuations.

## Key Features

### Real-Time Data Procurement
- Utilized Yahoo Finance API to fetch real-time stock data for Fortune 500 companies.
- Ensured data accuracy and completeness for robust analysis.

### Unsupervised Machine Learning Application
- Implemented the K-means clustering algorithm to group companies based on their daily stock price movements.
- Identified common patterns and trends among different clusters, providing valuable insights into stock market behavior.

### Statistical Modeling and Data Visualization
- Developed various statistical models using the Matplotlib library to enhance data analysis and interpretability.
- Created detailed visualizations to represent clustering results and stock price trends effectively.

Certainly! Here's how you can structure the instructions in Markdown language:

### Running the Project

#### Fetch Data:

1. **Script Execution:**
   - Execute the `data_fetching.py` script to fetch real-time stock data from Yahoo Finance and preprocess it for analysis.

   ```bash
   python data_fetching.py
   ```

2. **Notebook Interaction:**
   - Alternatively, you can run the `data_fetching.ipynb` notebook to interactively fetch and preprocess the data.

#### Perform Clustering Analysis:

1. **Script Execution:**
   - Execute the `clustering_analysis.py` script to apply the K-means clustering algorithm to the preprocessed data.

   ```bash
   python clustering_analysis.py
   ```

2. **Notebook Interaction:**
   - Alternatively, you can run the `clustering_analysis.ipynb` notebook to interactively perform clustering analysis.

#### Generate Visualizations:

1. **Script Execution:**
   - Execute the `visualization.py` script to create visualizations of the clustering results and stock price trends.

   ```bash
   python visualization.py
   ```

2. **Notebook Interaction:**
   - Alternatively, you can run the `visualization.ipynb` notebook to interactively generate and explore visualizations.

### Results

The project provides valuable insights into stock market behavior by categorizing Fortune 500 companies based on their daily stock price movements. The visualizations and clustering results can aid in making informed decisions regarding portfolio diversification, risk management, and sector analysis.
