import pandas as pd
import numpy as np

np.random.seed(42)
countries = np.random.random_sample(12);

# used in jupiter

df = pd.DataFrame()
df['country'] = countries
df