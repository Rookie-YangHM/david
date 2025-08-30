# 단위문제명
단계1 : 반달곰 커피 IT 혁신팀의 첫걸음

# 분야
컴퓨터공학

# 구분
DevOps일

# 문제기술
## 기술적 설명

<h1>수행과제</h1>
<h3>문제1 커피를 좋아하는 동료들을 위해서</h3>
<ul>
<li>Github 공식 문서 사이트에서 시작하기(빠른시작) 내용을 확인한다.</li>

> https://docs.github.com/ko  
> https://docs.github.com/ko/get-started  
> https://docs.github.com/ko/get-started/start-your-journey


<li>Github 사이트에 가입하고 로그인 한다.</li>
> 두 말 하믄 잔소리    

<li>Github의 유료 요금제와 무료 요금제의 차이점을 확인한다.</li>

> https://github.com/pricing  
> https://github.com/pricing#compare-features

<li>GitHub에서 토큰을 생성한다.</li>
> https://github.com/settings/tokens  

<li>이후에 토큰을 사용 확인 할 수 있게 텍스트 파일로 저장해둔다. 인증 후에 텍스트 파일은 삭제한다.</li>
> okay

<li>토큰 정보를 PC에 저장하여 GitHub 자동 로그인 되도록 설정한다.</li>

> **Windows:**
> 
> 제어판 > 사용자 계정 > 자격 증명 관리자 > Windows 자격 증명으로 이동  
> 'git: https://github.com' 또는 'GitHub' 자격 증명을 찾아 편집  
> 비밀번호 항목에 발급받은 토큰을 붙여넣고 저장
> 
> **macOS:**
> 
> 터미널에서 `git config --global credential.helper osxkeychain` 명령어를 실행하여 Keychain 사용을 설정  
> `git push` 또는 `git pull` 명령어를 실행하여 자격 증명을 입력  
> 입력한 자격 증명이 Keychain에 저장됨
> 
> **Linux:**
> 
> 터미널에서 `git config --global credential.helper store` 명령어를 실행하여 자격 증명을 파일에 저장
> `git push` 또는 `git pull` 명령어를 실행하여 자격 증명을 입력
> 입력한 자격 증명이 `~/.git-credentials` 파일에 저장됨
> 
> 
>>  **참고** at LINUX
>> 
>>  `.git-credentials` 파일을 삭제하거나,
>>  credential.helper store 설정 제거
>>  ```
>>  git config --global --unset credential.helper
>>  ```


</ul>
<h3>문제2 함께 일하는 즐거움을 위해서..</h3>
<ul>
<li>GitHub에서 원격 저장소를 david라는 이름으로 새로 만든다.</li>

> https://github.com/Rookie-YangHM/david.git

<li>app.py가 저장되어 있는 PC의 작업 디렉토리로 이동하여 원격 저장소를 origin이라는 이름으로 추가한다.</li>

> **…or create a new repository on the command line**
> ```
> echo "# david" >> README.md
> git init
> git add README.md
> git commit -m "first commit"
> git branch -M main
> git remote add origin https://github.com/Rookie-YangHM/david.git
> git push -u origin main
> ```
> **…or push an existing repository from the command line**
> ```
> git remote add origin https://github.com/Rookie-YangHM/david.git
> git branch -M main
> git push -u origin main
> ```
> 
> =>
> ```
> ## 경로이동
> cd <app.py가_있는_폴더_경로>
> 
> ## 원격 저장소(origin) 추가
> git remote add origin https://github.com/Rookie-YangHM/david.git
> ```


<li>PC의 저장소 main 브랜치의 커밋 내역을 원격저장소의 main 브랜치로 올린다.</li>

<li>PC의 저장소 add-image 브랜치의 커밋 내역을 원격저장소의 add-image 브랜치로 올린다.</li>
<li>추가한 두 개의 브랜치가 원격저장소에 잘 전달되었는지 확인한다.</li>
</ul>

>	[내 컴퓨터(로컬)]
>	 ├── main          ← 로컬 main 브랜치
>	 └── add-image     ← 로컬 add-image 브랜치
>	
>	          │  push / pull
>	          ▼
>	
>	[원격 저장소(origin, GitHub)]
>	 ├── origin/main       ← GitHub에 있는 main 브랜치
>	 └── origin/add-image  ← GitHub에 있는 add-image 브랜치

```bash
git branch
```

```bash
git branch add-image
```

```bash
git checkout add-image

#또는

git switch add-image
```

```bash
git add app.py
git commit -m "add image feature"
```

**동기화(push / pull)**
```bash
# 로컬 main → GitHub origin/main으로 업로드.
git push origin main 

# GitHub origin/main → 로컬 main으로 가져오기.
git pull origin main 

# 로컬 add-image → GitHub origin/add-image로 업로드.
git push origin add-image
```




<h3>문제3 소스코드 관리는 꼭 필요한 것만</h3>
<ul>
<li><p>GitHub david 원격 저장소에서 .gitignore 파일을 추가한다.</p>
</li>
<li><p>.gitignore 파일을 아래 내용으로 편집한다.</p>
<pre><code class="language-css">__pycache__
.venv</code></pre>
</li>
<li><p>원격 저장소로부터 코드를 내려받기 한다.</p>
</li>
<li><p>GitHub david 원격 저장소에 위 두개의 .gitignore에서 지정한 <strong>pycache</strong>, .venv 디렉토리가 있다면 삭제한다.</p>
</li>
<li><p>변경사항을 Git 커밋 후 원격저장소의 main 브랜치로 다시 올린다.</p>
</li>
</ul>

## 개발환경

<h1>개발환경</h1>
<ul>
<li>터미널에서 Git 기본 명령어만 사용 (GUI 툴 사용 금지)</li>
</ul>


## 제약조건

<h1>제약 사항</h1>
<ul>
<li>터미널에서 Git 기본 명령어만 사용 (GUI 툴 사용 금지)</li>
<li>원격 저장소는 Public으로 생성, 나머지는 기본 설정 유지</li>
</ul>
<h1>보너스 과제</h1>
<h3>문제 1: 인기 있는 오픈소스 Fork 및 토큰 관리 보안</h3>
<ul>
<li>Star가 100개 이상 달린 타인의 GitHub 저장소를 본인의 GitHub 계정으로 Fork 한다.</li>

```
참고 : 별 수로 검색 > 리포지토리 검색 - GitHub Docs
(https://docs.github.com/ko/search-github/searching-on-github/searching-for-repositories#search-by-number-of-stars)
```

> **검색 키워드**
>
> `stars:>=n` `language:LANGUAGE`



<li>Personal Access Token을 텍스트 파일로 저장한 뒤 삭제해야 하는 이유를 조사한다.</li>

#### GitHub Personal Access Token 관리 이유

##### 1. 토큰을 텍스트 파일로 저장하는 이유

-   발급 직후에는 한 번만 보여주기 때문에, 나중에 다시 확인할 수 없음
-   IDE, CLI, 자동화 스크립트 등에서 써야 할 때 안전하게 복사·붙여넣기
	위해 임시로 저장하는 것
-   기록해두지 않으면 새로 토큰을 발급해야 하는 번거로움이 있음

##### 2. 저장한 텍스트 파일을 삭제해야 하는 이유

-   토큰이 평문으로 남아 있으면 보안 리스크가 큼
-   다른 사람이 PC를 보거나, 백업/클라우드 동기화에 포함되면 유출 가능성 있음
-   Git 리포지토리에 실수로 커밋되면 즉시 악용될 수 있음 (공개 repo면 특히 위험)
-   따라서 사용 후에는 **안전한 비밀 저장소(예: OS 키체인, 비밀 관리
	서비스, GitHub CLI의 `gh auth login`)로 옮기고, 임시 텍스트 파일은
	삭제**하는 게 원칙임

##### 3. 안전한 대안

-   macOS / Linux: OS의 Keychain / Secret Service에 저장
-   Windows: Windows 자격 증명 관리자 사용
-   GitHub CLI (`gh`) 설치 후:

	``` bash
	gh auth login
	```

	→ 로컬에서 안전하게 PAT를 관리해줌
---- 

👉 정리: **텍스트 파일은 "임시 메모" 용도일 뿐, 영구 보관소가 아님.
삭제하지 않으면 그 파일이 곧 백도어가 될 수 있음.**

</ul>

<h3>문제 2: 저장소 복제</h3>
<ul>
<li>다른 PC나 디렉토리에서 원격 저장소를 clone 한다.</li>
</ul>
<h3>문제 3: 파이썬 프로젝트에서 .gitignore 사용 이유</h3>

> ### .gitignore 사용 이유
> 
> **불필요한 파일 제외**
> 
> - 빌드 결과물
> - 의존성 디렉토리/파일
> - S/에디터가 자동 생성하는 임시 파일
> 
> **보안유지**
> 
> **협업/효율**
> - 팀원끼리 공통으로 관리할 코드/리소스만 Git에 포함 → 깔끔한 리포지터리


<ul>
<li>파이썬 개발 시 <code>__pycache__</code>와 <code>.venv</code> 디렉토리가 생성되는 이유를 조사한다.</li>

> - __pycache__는 “파이썬이 실행 속도를 위해 자동으로 생성하는 캐시 저장소
> - .venv는 “특정 프로젝트만의 파이썬 실행 환경을 제공하는 가상 독립 공간”이다.

<li>GitHub에서 <code>.gitignore</code> 템플릿 중 <code>Python</code>을 선택했을 때 포함되는 항목을 확인한다.</li>

> - __pycache__/, *.pyc → 파이썬 실행 시 생기는 캐시 파일 무시
> - env/, .venv/ 등 → 가상환경 디렉토리 무시
> - build/, dist/ 등 → 빌드/배포 결과물 무시
> - .ipynb_checkpoints/ → 주피터 노트북 체크포인트 무시
> - .vscode/, .idea/ 등 → 개발 툴 설정 파일 무시
> - 테스트/커버리지 관련 파일(.tox/, .coverage)도 무시

```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Jupyter Notebook
.ipynb_checkpoints

# IDE/Editor 설정
.pydevproject
.project
.idea/
*.sublime-workspace
*.sublime-project
.vscode/

# MyPy, Pyre, Pytype
.mypy_cache/
.dmypy.json
dmypy.json
.pyre/
.pytype/

# Profiling data
.prof
```

<li>Flask 기반 프로젝트를 기준으로 <code>.gitignore</code>에 추가되어야 할 항목들을 나열한다.</li>

> - Python 공통: __pycache__/, .venv/, dist/, *.egg-info
> - Flask 특화: instance/, .env, SQLite DB 파일
> - 테스트/로그: .coverage, .pytest_cache/, *.log
> - IDE/OS: .vscode/, .idea/, .DS_Store


</ul>
