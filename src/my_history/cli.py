def hello_msg():
    return "hello"

def cmd():
    msg = hello_msg()
    print(msg)

    
# parser = argparse.ArgumentParser(description='print command count')
# parser.add_argument('-s','--count',action='store', help ='print counting insist command')
# parser.add_argument('-t','--countall',action='store', help='printing all commands count')
# parser.add_argument('-d','--date', action='store_true',help='Date you want')

# args = parser.parse_args()
# def cnt(q):
 #   df = read_parquet()
 #   df = pd.read_parquet("~/tmp/history.parquet") 
 #   df['dt'] = df['dt'].str.replace('^', '')
  #  df['cmd'] = df['cmd'].str.replace('^', '')
   # df['cnt'] = df['cnt'].str.replace('^', '')
  #  df['cnt'] = df['cnt'].astype(int)
  #  fdf = df[df['cmd'].str.contains(q)]
  #  cnt = fdf['cnt'].sum()
  #  return cnt

# def read_parquet(path="~/tmp/history.parquet"):
   # df = pd.read_parquet(path)
   # return df


#def query():
#        q = args.count
 #       i = cnt(q)
  #      print('질의:%s에 대한 결과는 %d입니다' %(q,i))

