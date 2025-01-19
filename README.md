# Analysis of the Distribution of Teaching Staff in Romania by Education Levels and Regions

This project, **"Analysis of the Distribution of Teaching Staff in Romania by Education Levels and Regions"**, applies clustering techniques to identify patterns and disparities in the distribution of teaching resources across the country. The study provides valuable insights for policymakers and stakeholders in the education sector to support strategic planning and resource allocation.

## Table of Contents

- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Methodology](#methodology)
- [Key Results](#key-results)
- [Conclusions](#conclusions)

## Project Description

The project focuses on analyzing and clustering data regarding the distribution of teaching staff across Romania based on:
- **Education levels**: Primary, secondary, and tertiary.
- **Geographical regions**: NUTS2 regions in Romania.

Using hierarchical clustering methods, the project highlights discrepancies and potential areas for improvement in the education system.

## Technologies Used

- **Programming Language**: Python
- **Libraries and Frameworks**:
  - `pandas`, `numpy` for data manipulation and analysis
  - `matplotlib`, `seaborn` for data visualization
  - `scipy` for hierarchical clustering
  - `scikit-learn` for silhouette analysis and clustering metrics
  - `geopandas` for spatial data visualization and mapping
  - `Jsoup` for data scraping (if additional data was required)
- **Geospatial Data**:
  - Shapefile for Romanian NUTS2 regions (e.g., `RO_NUTS2/Ro.shp`)

## Project Structure

├── data_in/ │ ├── personal_didactic_2023.csv # Input dataset │ └── RO_NUTS2/ # Shapefile for mapping ├── data_out/ │ ├── Ierarhie.csv # Hierarchical clustering results │ └── Partitii.csv # Cluster partitions ├── scripts/ │ ├── main_analysis.py # Main script for running the analysis │ ├── grafice.py # Custom functions for plotting and visualizations │ ├── functii.py # Helper functions for preprocessing and analysis ├── README.md # Project documentation └── requirements.txt # Python dependencies

## Methodology

1. **Data Preprocessing**:
   - Missing values were handled using a custom `nan_replace_t` function.
   - Observed variables were normalized and prepared for clustering.

2. **Clustering**:
   - Hierarchical clustering (`ward` method) was used to group regions based on similarities.
   - The "elbow" method and silhouette scores were applied to determine the optimal number of clusters.

3. **Principal Component Analysis (PCA)**:
   - PCA was performed to reduce dimensionality and visualize clusters in the first two principal components.

4. **Visualization**:
   - Dendrograms, silhouette plots, and scatter plots of clusters.
   - Histograms for each variable by cluster.
   - Maps illustrating the spatial distribution of clusters.

## Key Results

- Identified distinct clusters of regions based on the distribution of teaching staff by education levels.
- Highlighted regions with disparities in teaching resource allocation.
- Visualizations (e.g., maps, histograms) provide an intuitive understanding of the clustering results.

## Conclusions

This project demonstrates the power of clustering techniques for analyzing the distribution of teaching staff in Romania. By identifying patterns and regional disparities, the study provides actionable insights for improving resource allocation in the education sector. 

The methodology and results can be adapted to other domains or countries for similar analyses.

For any questions or suggestions, please feel free to open an issue or contact the author.
