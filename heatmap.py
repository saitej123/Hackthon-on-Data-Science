import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
ndf = pd.read_csv("bitcoin_dataset.csv")
sns.heatmap(result, annot=True, fmt="g", cmap='viridis')
plt.show()
