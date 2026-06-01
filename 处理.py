


import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(14, 5), dpi=120)

ax.plot(df['日期'], df['收盘'], label='收盘价', color='steelblue', linewidth=1.5)
ax.plot(df['日期'], df['MA5'], label='MA5', color='orange', linewidth=1, linestyle='--')
ax.plot(df['日期'], df['MA20'], label='MA20', color='red', linewidth=1, linestyle='--')

ax.set_title('贵州茅台(600519) 收盘价走势', fontsize=14)
ax.set_xlabel('日期')
ax.set_ylabel('价格（元）')
ax.legend()
ax.grid(True, alpha=0.3)

# 自动格式化x轴日期
fig.autofmt_xdate()

plt.tight_layout()
plt.savefig('output/price_trend.png', dpi=120)
plt.show()
print("图表已保存")