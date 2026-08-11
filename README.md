# DAG and CPM Implementation for F1 Honda RA621H Assembly Scheduling

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

This project implements the **Directed Acyclic Graph (DAG)** and **Critical Path Method (CPM)** to optimize the assembly scheduling and task dependency analysis of the Formula 1 Honda RA621H engine.

## Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Results and Visualization](#results-and-visualization)
- [License](#license)

## Overview

The assembly of a modern Formula 1 engine like the Honda RA621H is a highly complex process requiring precise scheduling. By representing the assembly tasks as a Directed Acyclic Graph (DAG), this project identifies the optimal topological order of assembly. Furthermore, the Critical Path Method (CPM) is applied to determine the minimum total time required and to pinpoint the critical tasks that cannot be delayed without delaying the entire project.

## Key Features

- **Data Processing**: Partition and clean raw assembly datasets.
- **Topological Sorting**: Implementation of Kahn's Algorithm to find valid assembly sequences.
- **CPM Calculation**: Calculation of Earliest Start Time (EST), Latest Start Time (LST), and slack for each task.
- **Graph Visualization**: Generation of network graphs to visually trace task dependencies.
- **Web Frontend**: Interactive visualization dashboard to explore the DAG and CPM results.

## Project Structure

```text
dag-cpm-honda-f1/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt               
├── archive/                       # Deprecated progress files and experiments
├── data/                          # Raw and processed datasets
│   └── Honda_RA621H_Assembly_Dataset.xlsx
├── docs/                          # Research papers and reference documents
├── notebooks/                     # Jupyter Notebooks for data exploration and modeling
│   ├── Notebook_Honda_RA621H_DAG_Kahn_CPM.ipynb
│   └── Notebook_DAG_Progress.ipynb 
├── results/                       # Generated outputs (graphs, CSV reports)
│   ├── graph/                     
│   └── output_csv/                
├── src/                           # Core Python scripts
│   └── partition_dataset.py       
└── web/                           # HTML/JS interactive visualization application
    ├── css/
    ├── data/
    ├── js/
    ├── py/
    └── index.html
```

## Prerequisites

- **Python 3.8+**
- Jupyter Notebook environment (e.g., JupyterLab or VS Code)
- Standard Data Science libraries (Pandas, NetworkX, Matplotlib)

## Installation and Setup

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/dag-and-cpm-implementation-for-f1-honda-ra621h-assembly-scheduling.git
   cd dag-and-cpm-implementation-for-f1-honda-ra621h-assembly-scheduling
   ```
2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Data Partitioning (Optional)
If you need to re-partition or preprocess the dataset, run the python script located in the `src` folder:
```bash
python src/partition_dataset.py
```
> **Note**: Be aware that running scripts or notebooks may require path adjustments depending on your execution directory. It is recommended to run everything from the project root.

### 2. Running the Analysis
Open the main Jupyter Notebook to view or re-run the Kahn's Algorithm and CPM analysis:
```bash
jupyter notebook notebooks/Notebook_Honda_RA621H_DAG_Kahn_CPM.ipynb
```
Follow the cells sequentially. The notebook will read from the `data/` folder and output results to the `results/` folder.

### 3. Web Visualization
To view the interactive graph dashboard:
1. Navigate to the `web/` directory.
2. Open `index.html` in any modern web browser.
*(For security reasons, some browsers may require you to serve the directory via a local HTTP server, e.g., `python -m http.server 8000`)*

## Results and Visualization

All generated artifacts from the notebook are stored in the `results/` directory:
- **`results/graph/`**: Contains static PNG renders of the full DAG and degree distributions.
- **`results/output_csv/`**: Contains the exported tables for components, dependency edges, and summary statistics.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
