import pandas as pd
import matplotlib.pyplot as plt
import pickle

# 讀取 CSV 檔案
data = pd.read_csv('./data.csv')

# 創建圖表
fig, ax = plt.subplots(figsize=(100, 100))  # Increase the figure size

# 繪製點並加上標記
for i, row in data.iterrows():
    m, n, f_value = row['m'], row['n'], row['f(m,n)']
    if f_value == 50123:
        color = 'red'
    else:
        color = 'blue'
    ax.scatter(m, n, color=color)
    ax.text(m, n, str(f_value), fontsize=9, ha='right')

# 設定坐標軸標籤
ax.set_xlabel('m')
ax.set_ylabel('n')

# 顯示圖表
# ax.set_title('Scatter Plot of (m, n) with f(m, n) labels')
ax.grid(True)

# Save the figure as a pickle file
with open('scatter_plot.pkl', 'wb') as f:
    pickle.dump(fig, f)

plt.savefig('scatter_plot.png', dpi=300)  # Save as PNG for reference
plt.show()