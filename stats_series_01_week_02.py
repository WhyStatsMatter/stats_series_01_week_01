# Snippet 1
import numpy as np

# Discrete data
pets = np.random.randint(0, 5, 10)  # 10 random integers between 0 and 5 (number of pets)

# Continuous data
weights = np.random.normal(70, 10, 10)  # 10 weights from a normal distribution with mean 70 and std deviation 10

# Snippet 2
import pandas as pd

# Ordinal data
sizes = pd.Categorical(["Small", "Medium", "Large", "Large", "Small", "Medium"],
                       categories=["Small", "Medium", "Large"], ordered=True)

# Nominal data
colors = pd.Categorical(["Red", "Blue", "Green", "Blue", "Red", "Green"])

# Snippet 3
# Binary data
success = np.random.choice([0, 1], size=100, p=[0.5, 0.5])  # 100 random successes/failures

# Snippet 4
# Time series data
dates = pd.date_range(start='1/1/2020', periods=100)  # 100 dates starting from 1/1/2020
values = np.random.normal(0, 1, 100)  # 100 random values from a standard normal distribution
time_series = pd.Series(data=values, index=dates)
