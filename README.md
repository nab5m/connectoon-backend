# 커넥툰
그림 작가와 스토리 작가, 함께 웹툰을 만들어볼 작가님을 만납니다 <br><br>
<b>Demo:</b> [커넥툰 api 서버](https://go.aws/3bm78Qx)<br>
<b>admin 계정:</b> nab5m / nab5m

## 개발 환경
<b>OS:</b> Windows 10 <br>
<b>DB:</b> PostgreSql 12 <br>
<b>IDE:</b> Pycharm 2019.2.x <br>
<b>Python:</b> 3.8.0 <br>
<b>pip:</b> 20.0.2 <br><br>

psycopg2-binary가 설치 안될 경우 pip를 최신 버전으로 업그레이드 했는지 확인해주세요. 리눅스의 경우 psycopg2로 대체할 수도 있습니다.<br>

## 프로젝트 fork or clone
```shell script
0. fork and clone this project
1. make your virtualenv directory
2. create file 'config/secret_settings.py'
<config/secret_settings.py>
  SECRET_KEY = 'make your django secret key'

  DB_NAME = 'your database name'
  DB_USERNAME = 'your database user name'
  DB_PASSWORD = 'your database user password'
  DB_HOST = 'localhost'
  DB_PORT = '5432'

3. pip install -r requirements.windows.txt
4. python manage.py migrate
5. python manage.py loaddata role.json 
6. python manage.py runserver

7. Open your brower and check if it's operating (http://127.0.0.1:8000)

8. happy coding :)
9. make pull requests for me
```

## 메모
배포 참고 자료
- https://wikidocs.net/6601#gunicorn_1

sudo vi /etc/postgresql/10/main/pg_hba.conf
# postgresql 인증 방식 수정

정적 파일(/assets/)는 nginx로 접속
나머지 처리는 gunicorn에 위임
