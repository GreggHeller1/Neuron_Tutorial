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

#settings
# %load_ext autoreload
# %autoreload 2

#installs (for colab only)


#local imports
from src import data_io as io
from src import plotting
from src import computation as comp


#imports
import xarray as xr
import pandas as pd
from matplotlib import pyplot as plt
import os

#define paths
test_path = os.path.join('demo_data', 'test.txt')
print(test_path)
print(os.getcwd())
os.path.exists(test_path)

# +
#data inputs
io.readfile(test_path)


# -

#data manipulation


#plots


#data output

