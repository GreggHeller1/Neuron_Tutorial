# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py,md
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# + [markdown] id="view-in-github" colab_type="text"
# <a href="https://colab.research.google.com/github/GreggHeller1/Neuron_Tutorial/blob/main/scripts/notebook.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# + id="71ee021b"
#settings
# %load_ext autoreload
# %autoreload 2
try:
  import google.colab
  in_colab = True
except:
  in_colab = False
print(in_colab)

# + colab={"base_uri": "https://localhost:8080/"} id="4e02e926" outputId="84475a29-508b-4d96-adf5-e85665e994d2"
#installs (for colab only, run this once)
if in_colab:
    # ! git clone https://github.com/GreggHeller1/Neuron_Tutorial.git


# + id="5e9731ca"
#local imports
#cwd if in colab for imports to work
if in_colab:
    # %cd /content/Neuron_Tutorial
    
from src import data_io as io
from src import plotting
from src import computation as comp


# + id="db51ef2e"
#imports
import xarray as xr
import pandas as pd
from matplotlib import pyplot as plt
import os

# + colab={"base_uri": "https://localhost:8080/"} id="a06b6e4a" outputId="989c69e2-c8c4-43e0-9ba6-7a36f66be4c3"
#define paths
#cwd if in colab for file loading to work
if in_colab:
    # %cd /content/Neuron_Tutorial/scripts
    
test_path = os.path.join('demo_data', 'test.txt')
print(test_path)
print(os.getcwd())
os.path.exists(test_path)

# + colab={"base_uri": "https://localhost:8080/"} id="b3586a50" outputId="56f159c6-3dbc-4b37-d217-083fb5d2e792"
#data inputs
io.readfile(test_path)



# + id="82a5927b"
#data manipulation


# + id="f700a7f6"
#plots


# + id="8dd23ba7"
#data output

