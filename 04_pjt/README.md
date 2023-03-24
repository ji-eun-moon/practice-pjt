# 230324 관통 프로젝트 4 - DB를 이용한 웹페이지 구현
## 프로젝트 목표
- 데이터를 생성, 조회, 수정, 삭제할 수 있는 Web application 제작
- Django web framework를 사용한 데이터 처리
- Django Model과 ORM에 대한 이해
- Django ModelForm을 활용한 사용자 요청 데이터 유효성 검증
- Django Static files 관리 및 image file 업로드
---
## base.html
- 정적 파일을 구성하고 사용하기 위해 base template에 템플릿 태그를 사용하고 지정된 경로에 있는 정적 파일의 URL을 참조하였다.
- 이 때 static file이 담긴 static 폴더는 앱 상위 폴더에 생성하였으며, 추가 경로를 설정하기 위해 settings에 STATICFILES_DIRS을 작성하였다.
## index.html
- view 함수 작성시 GET 요청만을 허용하기 위해 require_safe 데코레이터를 사용
- DB에 저장된 모든 영화를 불러온 다음 for문을 사용하여 전부 출력하도록 구현하였다.
## detail.html
- detail view 함수에서 받은 pk와 context를 사용하여 각각의 데이터를 출력하였다.
- 이미지를 업로드하지 않았을 경우 출력과정에서 발생할 수 있는 오류를 방지하기 위해 if문을 사용하여 이미지가 있을 경우에만 이미지를 출력 할 수 있도록 처리하였다.
- POST 요청시에만 파일을 삭제할 수 있도록 require_POST 데코레이터를 사용하여 delete view 함수를 작성하였다.
## create.html
- 게시물 작성 시 이미지가 업로드 되지 않는 문제가 발생하였었는데, enctype 속성을 변경해주지 않아서 발생한 문제였다.
    - multipart/form-data로 수정하였더니 해결 되었으며, update html에서도 마찬가지로 수정해주었다.
## update.html
- update 버튼을 눌렀을 때 [Reverse for 'update' with arguments '('',)' not found.] 에러가 발생하였다.
    - update view 작성시 context에 form만 적어주어서 발생한 것이었고, context = {'form': form,'movie': movie} 라고 수정해주었더니 해결 되었다. 
## CSS
- 버튼 색상을 바꿔주었다.

