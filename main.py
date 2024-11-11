import pandas as pd
import matplotlib.pyplot as plt

# 讀取 CSV 檔案
data = pd.read_csv('./data.csv')

# 創建圖表
plt.figure(figsize=(8, 6))

# 繪製點並加上標記
for i, row in data.iterrows():
    m, n, f_value = row['m'], row['n'], row['f(m,n)']
    plt.scatter(m, n, color='blue')
    plt.text(m, n, str(f_value), fontsize=9, ha='right')

# 設定坐標軸標籤
plt.xlabel('m')
plt.ylabel('n')

# 顯示圖表
plt.title('Scatter Plot of (m, n) with f(m, n) labels')
plt.grid(True)
plt.show()
