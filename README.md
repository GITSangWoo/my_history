# mah
- parquet 파일의 정보를 cli 기반으로 조회

## 사용법
```
$ my-history -s ls
ls 사용 횟수는 1234회 입니다.

$ my-history -t 10 -d 2024-07-17
  cmd  cnt
pyenv 4256
   cd 3472
  git 3396
mkdir 1932
  pip 1592
  cat 1368
   vi 1356
 sudo 1320
  pdm 1220
   rm 1104
```

### Dev env setting 

```
$ git clone <URL>
$ cd <PJT_NAME> 
$ pdm install 
$ [pdm test|pytest]


# option
$ pdm add -DG test pytest pytest-cov
```
### deploy
branch
```bash
$pip install git+https://github.com/GITSangWoo/my_history/tree/v0.2.0/argp
```
main
```bash
$pip install git+https://github.com/GITSangWoo/my_history.git 
```

### ref
```
pdm add https://github.com/GITSangWoo/my_history.git
pip install git+https://github.com/GITSangWoo/my_history.git
```
