
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
plt.style.use("ggplot")

def load_data(path="/home/olivera/Documents/side/", separator=",", index_col=0):

    """
    This function loads data and prepares it for the usage.

    """
    
    data = pd.read_csv(path, sep=separator, index_col=0)
    data = data.transpose()

    return data
