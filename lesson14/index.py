import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('avgiqpercountry.csv')

avg_iq_continent = df.groupby('continent')['average iq'].mean()

plt.figure(figsize=(10,6))

avg_iq_continent.plot(ind='line', marker='o', color='skyblue')

plt.title('avg iq per continent')
plt.xlabel('continent')
plt.ylabel('average iq')
plt. grid(axis="both", linestyle='--', alpha='0.7')
plt.show()

# filterd_df = df[df['average iq'] >= 100]
#
# filtered_df =filterd_df.sort_values(by='average iq', ascending=False)
#
# print(filterd_df)
#
# plt.figure(figuresize=(14,8))
#
# bars = plt.bar(filterd_df['country'], filtered_df['average iq'], color="skyblue")
#
# plt.title("average iq by country (iq >= 100", fontsize=16)
#
# plt.xlabel("country", fontsize=14)
# plt.ylabel("average iq", fontsize=14)
#
# plt.xticks(rotation=90, fontsize=10)
# plt.yticks(fontsize=10)
#
# plt.grind(axis='y', linestyle='--', alpha=0.8)
#
# plt.bar_label(bars, fnt="%.2f", fontsize=10, color='black')
#
# plt.tight_layout()
#
# plt.show()