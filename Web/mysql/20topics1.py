import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('docs-in-topics.csv')

# 当engine连接的时候我们就插入数据
engine = create_engine('mysql://root:123456@localhost/tfm?charset=utf8')
with engine.connect() as conn, conn.begin():
    df.to_sql('20topics', conn, if_exists='replace')
