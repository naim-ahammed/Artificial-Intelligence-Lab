# Modified K-Means Clustering (Manhattan Distance) with 2D Matrix Visualization
This project implements a modified version of the K-Means clustering algorithm using the **Manhattan distance** instead of the traditional Euclidean distance.  
It generates random 2D points and cluster centers, performs clustering, and visualizes the result using a simple 2D matrix printed directly to the console.


## Features
- Generates 100 random Cartesian points and 10 random cluster centers within a 20x20 grid.
- Clusters points using **Manhattan Distance** 
- Iteratively updates cluster centers based on the mean position of their assigned points.
- Visualizes the clustered data using a matrix printed with the `print()` function:
  - `P` represents a data point.
  - `C` represents a cluster center.
  - `.` represents an empty cell.


## Project Structure
- `kMeansClustering.py` — Main Python file containing the implementation of:
  - Data generation
  - Manhattan distance-based K-Means clustering
  - 2D matrix visualization using console output





