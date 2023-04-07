# 230407 5차 관통프로젝트 - 사용자 인증 기반 DB 설계
# 프로젝트 목표
- 데이터를 생성, 조회, 수정, 삭제할 수 있는 Web application 제작
- Django web framework를 사용한 데이터 처리
- Djnago Model과 ORM에 대한 이해
- Django Authentication System에 대한 이해
---
# 요구사항
- Django project : mypjt
- movies: 영화 데이터의 생성, 조회, 수정, 삭제가 가능한 애플리케이션
- accounts : 로그인, 로그아웃, 회원가입, 회원탈퇴, 회원정보수정, 비밀번호변경이 가능한 애플리케이션
## Form
### movies
- Movie 모델의 데이터 검증, 저장, 에러베시지, HTML을 모두 관리하기 위해 ModelForm을 사용하였다.
### accounts
- User 모델의 데이터 검증, 저장, 에러메시지, HTML을 모두 관리하기 위해 Forn, ModelForm, Custom ModelForm을 사용하였다.
- AUTH_USER_MODEL을 'accounts.User'로 대체하고 User class를 직접 참조하는 UserCreationForm과 UserChangeForm은 각각 커스텀 유저 모델을 사용하도록 커스텀해주었다. 
- CustomUserChangeForm 에서는 first_name과 last_name만 수정 가능하도록 field를 지정해주었다. 
## base.html
- 회원의 로그인 상태에 따라 요구사항에 맞게 다른 링크를 출력하도록 is_authenticated를 적용하였다.
- user 변수를 사용하여 현재 로그인 되어 있는 유저 정보를 출력하도록 하였다. 
## index.html
- 데이터베이스에 존재하는 모든 영화 제목을 표시하고, 영화제목을 클릭하면 detail.html로 이동할 수 있도록 하였다.
## detail
- 영화의 상세 정보 표시
- 영화의 수정, 삭제 버튼은 로그인 시에만 보이도록 is_authenticated을 적용하였다. 
- 전체 영화 목록 조회 페이지(index.html)로 이동하는 링크를 표시하였다. 
## create.html
- ModelForm을 사용하여 게시글 생성 페이지를 작성하였다. 
- 전체 영화 목록 조회 페이지(index.html)로 이동하는 링크를 표시하였다.
## update.html
- ModelFrom을 사용하여 게시글 수정 페이지를 작성하였다.
- input 요소에는 기존 데이터를 출력할수 있도록 instance를 요청받은 movie로 설정하였다.
- 수정사항을 제출하는 submit 버튼과 입력값을 초기값으로 재설정하는 reset 버튼을 표시하였다.
- 영화 상세정보 페이지(detail.html)로 이동하는 링크를 표시하였다.
## login.html
- AuthenticationForm을 사용하여 로그인 페이지를 작성하였다.
- view 함수 login과의 충돌을 방지하기 위해 import한 login 함수 이름을 auth_login으로 변경해서 사용하였다.
## signup.html
- CustomUserCreationForm을 사용하여 회원가입 페이지를 작성하였다.
- 회원가입 후 바로 로그인 될 수 있도록 로그인 함수를 사용하여 signup view 함수를 작성하였다. 
## update.html
- CustomUserChangeForm을 사용하여 회원정보 수정 페이지를 작성하였다.
## change_password
- PasswordChangeForm을 사용하여 비밀번호 변경 페이지를 작성하였다.
- 암호 변경시 세션 무효화를 방지하기 위해 update_session_auth_hash를 작성해주었다. 