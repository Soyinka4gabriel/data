import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Date': [
        '2023-12-14', '2023-12-15', '2023-12-16', '2023-12-17', '2023-12-18',
        '2023-12-19', '2023-12-20', '2023-12-21', '2023-12-22', '2023-12-23',
        '2023-12-24', '2023-12-25', '2023-12-26', '2023-12-27', '2023-12-28',
        '2023-12-29', '2023-12-30', '2023-12-31', '2024-01-01', '2024-01-02',
        '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', '2024-01-07'
    ],
    'Response Time (Minutes)':
    [11, 9, 12, 7, 14, 6, 11, 8, 10, 13, 5, 0, 12, 7, 11, 6, 14],
    'Resolution Time (Hours)': [
        2.25, 1.75, 2.5, 1.25, 3, 1, 2.25, 1.5, 2, 2.6, 1, 0, 2.5, 1.25, 2.25,
        1, 3
    ]
}

# Extend the data to have the same length
desired_length = 100
data['Date'].extend([''] * (desired_length - len(data['Date'])))
data['Response Time (Minutes)'].extend(
    [np.nan] * (desired_length - len(data['Response Time (Minutes)'])))
data['Resolution Time (Hours)'].extend(
    [np.nan] * (desired_length - len(data['Resolution Time (Hours)'])))

df = pd.DataFrame(data)

# Collect Data: Modify the data dictionary to include additional data points
data['Response Time (Minutes)'].extend([10, 12, 5, 9, 11] + [np.nan] * 5)
data['Resolution Time (Hours)'].extend([2, 2.4, 1, 1.75, 2.25] + [np.nan] * 5)

# Data Analysis
# Quantitative analysis
response_time_before = df['Response Time (Minutes)'][:10]
response_time_after = df['Response Time (Minutes)'][10:]

resolution_time_before = df['Resolution Time (Hours)'][:10]
resolution_time_after = df['Resolution Time (Hours)'][10:]

# Descriptive statistics
response_time_mean = df['Response Time (Minutes)'].mean()
response_time_std = df['Response Time (Minutes)'].std()
resolution_time_mean = df['Resolution Time (Hours)'].mean()
resolution_time_std = df['Resolution Time (Hours)'].std()
response_time_variance = df['Response Time (Minutes)'].var()
resolution_time_variance = df['Resolution Time (Hours)'].var()

print("\nDescriptive Statistics:")
print(f"Response Time Mean: {response_time_mean}")
print(f"Response Time Variance: {response_time_variance}")
print(f"Response Time Std: {response_time_std}")
print(f"Resolution Time Mean: {resolution_time_mean}")
print(f"Resolution Time Variance: {resolution_time_variance}")
print(f"Resolution Time Std: {resolution_time_std}")

# Trend calculation
response_time_trend = 'Increasing' if df['Response Time (Minutes)'].iloc[
    -1] > df['Response Time (Minutes)'].iloc[0] else 'Decreasing'
resolution_time_trend = 'Increasing' if df['Resolution Time (Hours)'].iloc[
    -1] > df['Resolution Time (Hours)'].iloc[0] else 'Decreasing'

print("\nTrend Calculation:")
print(f"Response Time Trend: {response_time_trend}")
print(f"Resolution Time Trend: {resolution_time_trend}")

# Calculate correlation
correlation = df['Response Time (Minutes)'].corr(df['Resolution Time (Hours)'])
print(
    f"\nCorrelation between Response Time (Minutes) and Resolution Time (Hours): {correlation}"
)

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Response Time (Minutes)'], df['Resolution Time (Hours)'])
plt.title('Scatter Plot of Response Time vs. Resolution Time')
plt.xlabel('Response Time (Minutes)')
plt.ylabel('Resolution Time (Hours)')
plt.grid(True)
plt.show()
