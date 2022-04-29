import os
import pandas as pd
list_ = os.listdir(r'C:\Users\OS\Desktop')
df = pd.DataFrame(list_)
df.to_csv('res.csv', header=False)  # 不加表头
##df.columns = ['line'+str(i) for i in range(10)]
##df.to_csv('res.csv', index=False)  # 添加表头



