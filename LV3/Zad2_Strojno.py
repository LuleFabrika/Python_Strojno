import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
mtcars = pd.read_csv('mtcars.csv')
print(mtcars)

mtcars.groupby('cyl')['mpg'].mean().plot.bar()
mtcars.boxplot(by='cyl',column='wt')
mtcars.boxplot(by='am',column='mpg')
mtcars.plot.scatter(x='qsec',y='hp',c='am',colormap='bwr')
plt.show()
