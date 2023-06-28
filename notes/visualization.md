# Visualization with matplotlib

The matplotlib package is a very expressive tool for generating a wide variety of visualizations in python.
* [matplotlib tutorial](https://matplotlib.org/stable/tutorials/introductory/index.html)
* [matplotlib gallery](https://matplotlib.org/stable/gallery/index.html)

## Installation
you need to install matplotlb using pip (or pip3 on mac)
``` bash
python -m pip install matplotlib   (ON Windows)
python3 -m pip install matplotlib   (ON Mac)
```
or
``` bash
pip install matplotlib ( on window)
pip3 install matplot  (on mac)
```
We will use it by import the pyplot function (and renaming in plt which is shorter)
``` python
from matplotlib import pyplot as plt
```
You can install it in a Jupyter lab notebook using the following code:
``` python
import sys
!{sys.executable} -m pip install matplotlib
```

## Basic use
The plt.plot function takes a list xs of x coordinate and list ys of y coordinates
and draws a line connecting the (x,y) points
``` python
xs = list(range(-10,11))
ys = [x*x for x in xs]
plt.plot(xs,ys)
```

You can also print histograms using plt.hist(vals)
and scatter plots with plt.scatter(xs,ys)
and bar charts with plt.bar(labels,vals)
