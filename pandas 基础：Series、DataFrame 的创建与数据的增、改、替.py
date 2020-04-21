import pandas as pd
import numpy as np
#1.
data1=np.random.randint(3,10,5)
s1=pd.Series(data1,index=list('abcde'))
print('s1=\n',s1)

#2.
s1.loc['c':]
s1.iloc[-3:]

#3.
s3=pd.DataFrame({'year':[2017,2018,2019],
                 'price':[10,20,30]})
print('\ns3=\n',s3)

#4.
data2=np.random.randint(5,15,15).reshape(5,3)
print('\ndata2=\n',data2)

df_test=pd.DataFrame(data2,index=['a', 'c', 'e', 'f', 'h'],
                     columns=['one', 'two', 'three'])
print('df_test=\n',df_test)

#5.
#将 a 行 one 列处替换成空值
df_test.loc['a','one']=np.nan
#将 c 行 two 列处替换成 -99
df_test.loc['c','two']=-99
#将 c 行 three 列处替换成 -99
df_test.loc['c','three']=-99
#将 a 行 two 列处替换成 -100
df_test.loc['a','two']=-100
#新增 four 列，值为 test
df_test['four']='test'
#重置索引为 ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
df_change=df_test.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print('\ndf_change=\n',df_change)

#6.
df_change.dropna()

#7.
df_change.dropna(how="all")

#8.
df_change.fillna(0)

#9.
df_change.drop_duplicates()