import argparse
from my_history.db.utils import read_data
from my_history.db.utils import top
from my_history.db.utils import count

def hello_msg():
    return "hello"

def cmd():
    msg = hello_msg()
   #  print(msg)
        
    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

    parser.add_argument('-s','--scount')
    parser.add_argument('-t', '--top') 
    parser.add_argument('-d', '--dt') 
    parser.add_argument('-p', '--pretty', action='store_true')
    

    args = parser.parse_args()
    # print(args.scount, args.top, args.dt, args.pretty)

    if args.scount:
      #  print(f"-s => {args.scount}")
        # TODO 명령어 카운트
        a=count(args.scount)
        print(f'{args.scount}사용 횟수는 {a}회 입니다.')
    elif args.top:
       #  print(f"-t => {args.top}")
        if args.dt: 
          #  print(f"-d => {args.dt}")
            a=top(int(args.top),args.dt)
            # TODO 특정 날짜의 명령어 TOP N
            if args.pretty:
                # 이쁘게 출력 
                a=top(int(args.top),args.dt,args.pretty)
                print(a)
            else:
                # 그냥 출력
                print(a)
        else:
            print(f"TODO - 에러나 안내 메시지를 주면")
            # parser.print_help()
            parser.error("-t 옵션은 -d 옵션과 함께 사용하시오!")
    else:
        parser.print_help()
        # TODO - 아용법을 출력한다. 


