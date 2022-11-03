# Load packages
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
sns.set_style('darkgrid')

from dataset import get_dataset


X, y = get_dataset('titanic')

g = sns.PairGrid(X)
g.map(sns.scatterplot)


