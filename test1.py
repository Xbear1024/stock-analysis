import akshare as ak
import pandas as pd
import os
# 获取贵州茅台近一年日线数据

df = ak.stock_zh_a_hist(symbol="600519", period="daily",
                         start_date="20260101", end_date="20260531")
df.to_csv("data/600519_data.csv", index=False)
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)