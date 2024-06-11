import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data
data = {
    'Date': [
        '2023-11-01', '2023-11-02', '2023-11-03', '2023-11-04', '2023-11-05',
        '2023-11-06', '2023-11-07', '2023-11-08', '2023-11-09', '2023-11-10'
    ],
    'Response Time (Minutes)': [
        15, 10, 12, 8, 9, 14, 7, 12, 8, 11
    ],
    'Resolution Time (Hours)': [
        2.75, 1, 2.25, 1.5, 1.75, 2, 1.25, 2.5, 2, 2.5
    ]
}

# Extend the data to have the same length
desired_length = 100
data['Date'].extend([''] * (desired_length - len(data['Date'])))
data['Response Time (Minutes)'].extend([np.nan] * (desired_length - len(data['Response Time (Minutes)'])))
data['Resolution Time (Hours)'].extend([np.nan] * (desired_length - len(data['Resolution Time (Hours)'])))

df = pd.DataFrame(data)

# Collect Data: Modify the data dictionary to include additional data points
data['Response Time (Minutes)'].extend([13, 9, 11, 7, 8] + [np.nan] * 5)
data['Resolution Time (Hours)'].extend([2.25, 1.5, 2, 1.25, 1.5] + [np.nan] * 5)

# Data Analysis
# Quantitative analysis
response_time_before = df['Response Time (Minutes)'][:10]
response_time_after = df['Response Time (Minutes)'][10:]

resolution_time_before = df['Resolution Time (Hours)'][:10]
resolution_time_after = df['Resolution Time (Hours)'][10:]

# Qualitative analysis
# Add code to conduct qualitative analysis with interview data

# Identify Influencing Factors
# Add code to identify and analyze key factors influencing the successful integration and utilization of the system

# Compare Organizations
# Add code to compare support service outcomes between organizations that implemented the system and those that did not

# Draw Conclusions
# Add code to draw conclusions based on the analysis of data

# Descriptive statistics
response_time_mean = df['Response Time (Minutes)'].mean()
response_time_std = df['Response Time (Minutes)'].std()
resolution_time_mean = df['Resolution Time (Hours)'].mean()
resolution_time_std = df['Resolution Time (Hours)'].std()

print("Descriptive Statistics:")
print(f"Response Time Mean: {response_time_mean}")
print(f"Response Time Std: {response_time_std}")
print(f"Resolution Time Mean: {resolution_time_mean}")
print(f"Resolution Time Std: {resolution_time_std}")

# Calculate correlation
correlation = df['Response Time (Minutes)'].corr(df['Resolution Time (Hours)'])
print(f"Correlation between Response Time (Minutes) and Resolution Time (Hours): {correlation}")

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Response Time (Minutes)'], df['Resolution Time (Hours)'])
plt.title('Scatter Plot of Response Time vs. Resolution Time')
plt.xlabel('Response Time (Minutes)')
plt.ylabel('Resolution Time (Hours)')
plt.grid(True)
plt.show()
