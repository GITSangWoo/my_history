import pandas as pd
import sys 

def cnt():
    command = (sys.argv[1])
    df = pd.read_parquet("~/tmp/history.parquet")
    df['dt'] = df['dt'].str.replace('^', '')
    df['cmd'] = df['cmd'].str.replace('^', '')
    df['cnt'] = df['cnt'].str.replace('^', '')
    df['cnt'] = df['cnt'].astype(int)
    fdf = df[df['cmd'].str.contains(command)]
    cnt = fdf['cnt'].sum()
    print(cnt)

