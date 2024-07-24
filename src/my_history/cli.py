import pandas as pd
import sys 

def cnt(q):
    df = read_parquet()
    df = pd.read_parquet("~/tmp/history.parquet") 
    df['dt'] = df['dt'].str.replace('^', '')
    df['cmd'] = df['cmd'].str.replace('^', '')
    df['cnt'] = df['cnt'].str.replace('^', '')
    df['cnt'] = df['cnt'].astype(int)
    fdf = df[df['cmd'].str.contains(q)]
    cnt = fdf['cnt'].sum()
    return cnt

def read_parquet(path="~/tmp/history.parquet"):
    df = pd.read_parquet(path)
    return df


def query():
    q = sys.argv[1]
    i = cnt(q)
    print(f'질의:{q}에 대한 결과는 {i}입니다')
    print('질의:%s에 대한 결과는 %d입니다' %(q,i))
    print('질의:%10s에 대한 결과는 %d입니다' %(q,i))
    print('질의:%10s에 대한 결과는 %d입니다' %(q,i))
