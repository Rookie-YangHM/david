# 과정3 : 단계1 : 가상머신 구축

노션 : [https://www.notion.so/3-1-25f62aa43a7d802993bade16a2d3f038](https://www.notion.so/3-1-25f62aa43a7d802993bade16a2d3f038)

# 수행과제

### 문제1. 가상머신 구축

- 무료 하이퍼바이저(VMWare, Hyper-V 등)를 설치한다.
- 이름이 `DevOps`인 가상머신을 생성하고, Ubuntu Desktop 20.04 LTS를 기본 설정으로 설치한다.
- 메모리 8192MB, 디스크 128GB로 설정한다.
- root 계정의 비밀번호를 설정한다.
- `apt-get update`, `apt-get upgrade`를 수행한다.
- 터미널에서 다음 정보를 확인한다:
    - 현재 사용 중인 쉘
    - 사용 가능한 쉘 목록

[풀이1.](https://www.notion.so/1-25f62aa43a7d801fb523ccbd3efd91c3?pvs=21)

### 문제2. 리눅스 명령어 실습

- `man` 명령어로 다음 명령어의 설명을 확인한다: `pwd`, `cd`, `ls`, `mkdir`, `rm`, `cp`, `mv`, `touch`
- 다음 디렉토리 및 파일 작업을 수행한다:
    - 홈 디렉토리에서 `tmp1`, `tmp2` 디렉토리를 생성한다.
    - `tmp1` 디렉토리 안에 `tmpfile1`, `tmpfile2` 파일을 생성한다.
    - `tmpfile2`를 `tmp2`로 복사하고, `tmp1`에서는 삭제한다.
    - `tmp1`을 `tmp2`로 이동한다.
- 최종 디렉토리 구조를 확인한다:
    - `~/tmp2/` 아래에 `tmpfile2`, `tmp1/`이 있으며 `tmp1/`에는 `tmpfile1`이 존재해야 한다.

[풀이2.](https://www.notion.so/2-25f62aa43a7d8099a947fe0258f0962a?pvs=21)

### 문제3. 리눅스 계정 관리

- `/etc/passwd` 파일을 확인하여 계정 목록을 확인한다.
- `sudo adduser testuser` 명령으로 새 계정을 생성한다.
- `su testuser`로 계정 전환 후 홈 디렉토리로 이동하여 파일 목록을 확인한다.
- `grep testuser /etc/passwd`로 현재 사용하는 쉘 확인
- `chsh -s /bin/dash testuser`로 쉘을 변경하고 반영 여부 확인
- `exit` 또는 기존 계정명으로 `su` 전환하여 원래 계정으로 복귀한다.

[풀이3.](https://www.notion.so/3-25f62aa43a7d80f9977edf92b9205105?pvs=21)

### 문제4. Git 설치 및 설정

- Git이 설치되어 있지 않으면 `apt`로 설치하고 최신 버전으로 업데이트한다.
- 다음 전역 설정을 적용한다:
    - `autocrlf`를 `input`으로 설정
    - 사용자 이름은 `_VM` 접미사를 포함하여 설정
    - 이메일 주소 설정
    - 기본 브랜치를 `main`으로 지정
- 다음 명령어로 설정 확인:
    - `git config --global --list`
    - `git config --global -e`로 에디터에서 설정 열기

[풀이4.](https://www.notion.so/4-25f62aa43a7d8021ba41c45dcd93b8b9?pvs=21)

### 문제5. Python 및 Flask 웹 서버 실행

- Python 3.8 이상이 설치되어 있는지 확인하고, 없는 경우 설치한다.
- `pip` 설치 후 `flask`, `gtts` 패키지를 설치한다.
- `vim`을 설치한 뒤, `vi` 에디터를 사용하여 홈 디렉토리에 아래 Python 코드를 작성한다:
    
    ```python
    from flask import Flask
    
    app = Flask(__name__)
    
    @app.route("/")
    def home():
        return "Hello, DevOps!"
    
    if __name__ == '__main__':
        app.run('0.0.0.0', 8080)
    ```
    
- Python 서버를 실행하고 Firefox 브라우저에서 `Hello, DevOps!`가 출력되는지 확인한다.

[풀이5.](https://www.notion.so/5-25f62aa43a7d804bb5e0f0a33c287f35?pvs=21)

### 개발환경

- 모든 작업은 **가상머신에서 Ubuntu Desktop 20.04 LTS 환경**에서 수행한다.
- **WSL은 사용 금지**이며, 하이퍼바이저는 반드시 무료 버전을 사용한다.
- **Ubuntu 터미널 및 vi 에디터**만 사용하며 별도 GUI 툴은 사용하지 않는다.
- 해당 문제들은 개인 PC에서만 허용합니다.

### 보너스 과제

- 각 문제별 문서 작성 과제:
    - 하이퍼바이저, 리눅스 배포판, 커널, 쉘 종류 및 특징
    - 리눅스 명령어, 디렉토리 구조 설명
    - 계정 관련 명령어 비교 (`adduser` vs `useradd`, `su` vs `sudo`)
    - Git 설치 방식 차이, `apt` vs 수동
    - 리눅스 에디터 종류, `vim` vs `vi`, vi 모드 및 명령어 설명

[과제 풀이](https://www.notion.so/25f62aa43a7d80f1828fc4c8f00e791d?pvs=21)

