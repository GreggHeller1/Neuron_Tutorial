---
jupyter:
  jupytext:
    formats: ipynb,py,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.8
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

```python
#settings
%load_ext autoreload
%autoreload 2
```

```python
#installs (for colab only)

```

```python
#local imports
from src import data_io as io
from src import plotting
from src import computation as comp

```

```python
#imports
import xarray as xr
import pandas as pd
from matplotlib import pyplot as plt
import os
```

```python
#define paths
test_path = os.path.join('demo_data', 'test.txt')
print(test_path)
print(os.getcwd())
os.path.exists(test_path)
```

```python
#data inputs
io.readfile(test_path)


```

```python
#data manipulation

```

```python
#plots

```

```python
#data output

```
