import pandas as pd
import argparse 


def cmd():
    msg = hello_msg()
    print(msg)

    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

    parser.add_argument('-c', '--count',action='store')      # option that takes a value
    parser.add_argument('-t', '--tail',action='store')      # option that takes a value
    parser.add_argument('-d', '--date', action='store')  # on/off flag     
    args = parser.parse_args()
    
    if  




def query(command):
        q = command 
        i = cnt(q)
        print('질의:%s에 대한 결과는 %d입니다' %(q,i))

def cnt(q):
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

def all_cnt(command)

print(query(args.count)) 
