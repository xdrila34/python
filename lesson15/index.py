import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('temperature_data.csv', parse_dates=['Date'])

# 1. Temperature Overview
total_avg_temp = df['Temperature'].mean()
print(f'Overall Average Temperature: {total_avg_temp:.2f}')

# 2. Monthly Temperature
df['Month'] = df['Date'].dt.month
monthly_avg_temp = df.groupby('Month')['Temperature'].mean()
print(monthly_avg_temp)

# Plot monthly average temperature
plt.figure(figsize=(10, 5))
monthly_avg_temp.plot(kind='bar', color='skyblue')
plt.xlabel('Month')
plt.ylabel('Average Temperature')
plt.title('Monthly Average Temperature')
plt.show()

# 3. Highs and Lows
hottest_day = df.loc[df['Temperature'].idxmax()]
coldest_day = df.loc[df['Temperature'].idxmin()]
print(f'Hottest Day: {hottest_day}')
print(f'Coldest Day: {coldest_day}')
# 4. Temperature Trends
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Temperature'], linestyle='-', marker='o', color='r')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Temperature Trends Over Time')
plt.xticks(rotation=45)
plt.show()

# 4b. Seasonal Average Temperature
df['Season'] = df['Date'].dt.month % 12 // 3 + 1
seasonal_avg_temp = df.groupby('Season')['Temperature'].mean()
print(seasonal_avg_temp)