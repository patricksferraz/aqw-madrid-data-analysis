# aqw-madrid-data-analysis
Analysis of air quality and weather data, madrid

## Installing

### With pip

```
pip install -r requirements.txt
```

### With anaconda

```
conda env create --file requirements.yml
```

### Build jupyter

```
export NODE_OPTIONS=--max-old-space-size=4096

# Jupyter widgets extension
jupyter labextension install @jupyter-widgets/jupyterlab-manager@1.1 --no-build

# jupyterlab renderer support
jupyter labextension install jupyterlab-plotly@1.3.0 --no-build

# FigureWidget support
jupyter labextension install plotlywidget@1.3.0 --no-build

# Build extensions (must be done to activate extensions since --no-build is used above)
jupyter lab build
```

## Starting

```
jupyter-lab
```
