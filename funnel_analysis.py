import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Marketing Funnel Stage Setup
funnel_stages = ['1. Ad Impressions', '2. Website Visits', '3. Lead Generation', '4. Product Trial', '5. Paid Conversion']
stage_counts = [250000, 45000, 12500, 3200, 850]

df = pd.DataFrame({
    'Funnel_Stage': funnel_stages,
    'User_Count': stage_counts
})

# 2. Conversion & Drop-off Calculations
df['Overall_Conversion (%)'] = (df['User_Count'] / df['User_Count'].iloc[0] * 100).round(2)
df['Step_Conversion (%)'] = (df['User_Count'] / df['User_Count'].shift(1).fillna(df['User_Count'].iloc[0]) * 100).round(2)
df['Step_Dropoff (%)'] = (100 - df['Step_Conversion (%)']).round(2)

print("=" * 60)
print("       MARKETING FUNNEL CONVERSION PERFORMANCE REPORT       ")
print("=" * 60)
print(df.to_string(index=False))
print("=" * 60)

# 3. Data Visualization
plt.figure(figsize=(10, 5))
sns.set_theme(style="white")

palette = sns.color_palette("viridis", len(df))
ax = sns.barplot(data=df, y='Funnel_Stage', x='User_Count', palette=palette)

# Annotate metrics on bars
for i, (count, step_conv) in enumerate(zip(df['User_Count'], df['Step_Conversion (%)'])):
    ax.text(count + 2000, i, f"{count:,} ({step_conv}% retained)", va='center', fontweight='bold', fontsize=10)

plt.title('End-to-End Marketing Funnel Performance', fontsize=13, fontweight='bold')
plt.xlabel('Number of Users')
plt.ylabel('Funnel Stage')
plt.xlim(0, 300000)
plt.tight_layout()
plt.savefig('funnel_performance_chart.png', dpi=300)
plt.close()

print("\n[SUCCESS] Visualizations saved to 'funnel_performance_chart.png'.")
