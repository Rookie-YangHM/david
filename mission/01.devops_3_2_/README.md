# 과정3 : 단계2 : 개발환경의 확인

노션 : [https://www.notion.so/3-2-25f62aa43a7d80648fbfcbcb7824f36d](https://www.notion.so/3-2-25f62aa43a7d80648fbfcbcb7824f36d)

# 수행과제

### 문제6. 개발환경의 확인

- 과제2에서 생성한 GitHub 토큰을 가상머신에 저장하여 GitHub 자동 로그인을 설정한다.
- 홈 디렉토리에 `david` 원격 저장소를 `git clone`으로 복제한다.
- `cd david`로 해당 디렉토리로 이동한다.
- `app.py`를 `python` 명령어로 실행한다. (`flask run` 사용 금지)
- Firefox 브라우저로 `http://127.0.0.1`에 접속하여 결과(`Hello, DevOps!` 또는 `Hello, 학습자 이름`)를 확인한다.

### 문제7. 리눅스 네트워크 실습

- `app.py`가 실행 중인 상태에서 아래 작업을 수행한다.
- Ubuntu에서 **Listen 중인 포트** 목록을 확인한다.
- `man` 명령어로 다음 명령어 설명을 확인한다: `ifconfig`, `curl`, `top`, `ps`, `kill`
- 다음 내용을 확인하고 조치한다:
    - `ip addr` 명령어로 가상머신의 IP 주소를 확인한다.
    - `curl` 명령어로 `127.0.0.1`과 가상머신 IP 주소 각각에서 요청 결과를 확인한다.
    - `ps -ef` 또는 `top` 명령어로 실행 중인 Python 프로세스를 확인한다.
    - `kill` 명령어로 해당 Python 프로세스를 종료하고, 정상 종료되었는지 확인한다.
- 변경 사항을 커밋하고 `main` 브랜치로 push 한다.

## 문제8. 시스템 서비스 등록

- `david` Flask 애플리케이션을 systemd 서비스로 등록한다.
- `/lib/systemd/system/david.service` 파일을 생성하고 다음과 같이 정의한다:
    
    ```css
    [Unit] Description=david flask server.
    After=syslog.target network.target
    
    [Service] WorkingDirectory=/home/&lt;사용자명&gt;/david
    ExecStart=python3 app.py
    Restart=always
    RestartSec=5s
    
    [Install] WantedBy=multi-user.target
    ```
    
- 다음 명령어로 서비스를 등록하고 실행한다:
    
    ```css
    sudo systemctl daemon-reload
    sudo systemctl enable david.service
    sudo systemctl start david.service
    ```
    
- `systemctl is-active david` 명령어로 서비스 상태가 **active**인지 확인한다.
- 웹브라우저로 접속해 결과를 확인한다.
- 테스트 완료 후 `sudo systemctl stop david.service` 명령어로 서비스를 중지한다.