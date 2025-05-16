# Air Quality and Weather Analysis in Madrid (2001-2016)

[![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Jupyter](https://img.shields.io/badge/Jupyter-1.2.3-orange.svg)](https://jupyter.org/)

## Overview

This project analyzes air quality and weather data in Madrid from 2001 to 2016. It provides interactive dashboards and in-depth statistical analysis using Python, Dash, Plotly, and Jupyter. The analysis includes data wrangling, exploratory data analysis, and interactive visualizations to help understand environmental trends in Madrid.

## Key Features

- **Interactive Dash Web App**: Visualize air quality and weather stations on an interactive map.
- **Jupyter Notebook Analysis**: Comprehensive exploratory data analysis and statistical insights.
- **Data Wrangling**: Preprocessing and analysis of large time series datasets.
- **Open Source**: Fully reproducible and extensible for community contributions.

## Demo

Check out the demo video in the `docs` folder: [video.mp4](docs/video.mp4)

## Table of Contents

- [Air Quality and Weather Analysis in Madrid (2001-2016)](#air-quality-and-weather-analysis-in-madrid-2001-2016)
  - [Overview](#overview)
  - [Key Features](#key-features)
  - [Demo](#demo)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Environment Setup](#environment-setup)
    - [Installation](#installation)
      - [With pip](#with-pip)
      - [With Anaconda](#with-anaconda)
    - [JupyterLab Setup](#jupyterlab-setup)
  - [Usage](#usage)
    - [Starting the Dash App](#starting-the-dash-app)
    - [Running the Jupyter Notebook](#running-the-jupyter-notebook)
  - [Project Structure](#project-structure)
  - [Data Sources](#data-sources)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)
  - [Contact](#contact)

## Getting Started

### Prerequisites

- Python 3.6 or higher
- pip or Anaconda
- Mapbox account and access token

### Environment Setup

1. Create a `.env` file in the project root:
```bash
touch .env
```

2. Add your Mapbox token to the `.env` file:
```bash
MAPBOX_TOKEN=your_mapbox_token_here
```

### Installation

#### With pip

```bash
pip install -r requirements.txt
```

#### With Anaconda

```bash
conda env create --file requirements.yml
```

### JupyterLab Setup

```bash
export NODE_OPTIONS=--max-old-space-size=4096

# Jupyter widgets extension
jupyter labextension install @jupyter-widgets/jupyterlab-manager@1.1 --no-build

# jupyterlab renderer support
jupyter labextension install jupyterlab-plotly@1.3.0 --no-build

# FigureWidget support
jupyter labextension install plotlywidget@1.3.0 --no-build

# Build extensions
jupyter lab build
```

## Usage

### Starting the Dash App

```bash
python app.py
```

### Running the Jupyter Notebook

```bash
jupyter-lab
```

## Project Structure

- `app.py`: Main Dash application for interactive visualizations.
- `analytics.ipynb`: Jupyter notebook for data analysis and visualizations.
- `dataset/`: Contains the air quality and weather data files.
- `docs/`: Documentation and demo video.
- `requirements.txt` and `requirements.yml`: Dependency management files.
- `.env`: Environment variables file (not tracked in git).

## Data Sources

- **Weather Data**: Barajas Airport, Madrid (1997–2015), sourced from The Weather Company.
- **Air Quality Data**: Madrid city stations (2001–2016).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Original data providers: The Weather Company and Madrid city air quality monitoring stations.

## Contact

- GitHub: [patricksferraz](https://github.com/patricksferraz)
