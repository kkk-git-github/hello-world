import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.figrue()
X = np.array("Example1")
Y = pd.DataFrame.drop(X).value

plt.scatter(X, Y)
plt.show()