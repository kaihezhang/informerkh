import os

import pandas as pd

from My_Informer import My_Informer
from models.My_Index import My_Index
from models.My_Visual import My_Visual
from models.TimeTrans import TimeTrans

"""确定实验参数"""
train_set = 0.8
filename='datasum.csv'
savedf = pd.DataFrame()
savedf['method'] = ['Informer']
savedf['train_set'] = [str(train_set)]
savedf['filename'] = [str(filename)]
print('\nparameters is : \n', savedf)
savedf.to_csv(path_or_buf='parameters\\parameters.csv', header=True, index=False, encoding='utf-8')

"""创建指定文件夹"""
filepath = 'results\\forecast'
if not os.path.exists(filepath):
    os.mkdir(filepath)

"""数据准备"""
df = pd.read_csv('data\\data_sum_delete.csv')
df.to_csv(path_or_buf='data\\ETT\\column_data.csv', header=True, index=False, encoding='utf-8')

"""数据预测"""
TimeTrans()
My_Informer()
My_Visual()
My_Index()
