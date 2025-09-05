# 과정2 : 단계1 : 협업시 충돌(자동 병합)

# 수행과제

### 문제1. 협업 시 충돌 – 자동 병합

- 로컬 작업 디렉토리의 `templates/menu.html` 파일에 `<hr>` 구분선을 추가한다.
	```html
	<center>
	메뉴판<p>
	<button name="menu1" style="width:70pt;">아메리카노</button><br>
	<button name="menu2" style="width:70pt;">카페라떼</button><br>
	</p><hr>
	<button name="menu2" style="width:70pt;">녹차</button>
	```
- 작업 디렉토리에서 스테이징 영역에 추가 및 저장소에 커밋 한다.
- GitHub 원격 저장소 사이트에서 둥글레차 메뉴를 추가한다.
	```html
	 <center>
	메뉴판<p>
	<button name="menu1" style="width:70pt;">아메리카노</button><br>
	<button name="menu2" style="width:70pt;">카페라떼</button><br>
	<button name="menu2" style="width:70pt;">녹차</button><br>
	<button name="menu2" style="width:70pt;">둥글레차</button>
	```
- 웹 상에서 Commit changes 후 push 한다.
- 로컬 저장소에서 원격 저장소로 push를 시도하고 에러 메시지를 확인한다.
- 이후 원격 저장소로부터 pull을 수행하고 병합 메시지를 확인한다.
- 병합된 `menu.html`의 결과를 확인하고, 다시 커밋한 후 원격 저장소로 push 한다.
- GitHub에서 병합된 결과가 정상 반영되었는지 확인한다.

### 문제2. 협업 시 충돌 – 동일 위치 충돌

- 로컬 `app.py`에 아래 코드를 추가하고 커밋한다.
	```html
	@app.route("/test1")
	def test1():
	    return render_template('test1.html')
	```
- GitHub 웹에서도 동일 위치에 아래 코드를 추가하고 커밋한다.
	```html
	@app.route("/test2")
	def test2():
	    return render_template('test2.html')
	```
- 로컬에서 push 시도 후 에러 메시지를 확인한다.
- 이후 pull 시도 후 충돌 메시지를 확인하고, Visual Studio Code에서 충돌 지점을 확인한다.
- 충돌을 수동으로 해결하고 상태를 확인한다.
- 수정 내용을 스테이징하고 커밋한 후 push 한다.
- 최종적으로 GitHub에서 병합된 결과를 확인한다.

### 문제3. 협업 시 충돌 – 강제 push

- 문제 2번에 상황을 다시 재현한다.
- 이번에는 수정이 아닌 로컬에서 강제로 push 한다.
	```css
	git push --force
	```
- GitHub에서 최종 `app.py`의 상태를 확인한다.

# **개발환경**

- 외부 툴(GUI Git 도구 등)은 사용하지 않는다.

# **제약사항**

- 코드 편집 및 충돌 해결은 반드시 **Visual Studio Code**에서 수행한다.
- Git 관련 작업은 모두 **터미널에서 기본 제공 명령어**만을 사용한다.
- 외부 툴(GUI Git 도구 등)은 사용하지 않는다.