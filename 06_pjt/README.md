# 230414 관통 프로젝트 6 - 관계형 데이터베이스 설계
## 프로젝트 목표
- Database many to one relationship(1:N)에 대한 이해
    - CRUD 보완하기 (Article - User)
    - 댓글 기능 구현하기 (Comment - Movie, Comment - User)
- many to many relationship(M:N) 에 대한 이해
    - 좋아요 기능 구현하기 (Movie - User)
    - 팔로우 기능 구현하기 (User - User)
---
# CRUD
## 모델 관계 설정
- 0개 이상의 게시글은 1개의 회원에 의해 작성될 수 있다. (N:1)
    - Article(N) - User(1)
### Article - Model
- Article 모델에 User 모델을 참조하는 외래키를 작성하였다.
    - User 모델을 참조하기 위해 `settings.AUTH_USER_MODEL`를 사용하였다.
    - 외래키가 참조하는 객체가 사라졌을 때 이를 참조하는 객체도 삭제하기 위해 on_delete 옵션 값을 CASCADE로 설정해주었다.
## CREATE
- ArticleForm 출력시 create 템플릿에서 불필요한 필드(user)가 출력되지 않도록 출력 필드를 title과 description으로 설정해주었다. 
- 외래키에 작성자 정보를 저장하기 위해 게시글 작성시 작성자 정보가 저장될 수 있도록 save의 commit 옵션을 활용하여 create 함수를 수정해주었다. 
## DELETE, UPDATE
- 게시글 삭제/수정을 요청하는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 삭제할 수 있도록 delete 함수를 수정해주었다. 
    - 추가로 해당 게시글의 작성자가 아니라면 detail 페이지에서 if 태그를 활용하여 게시글 수정/삭제 버튼을 출력하지 않도록 하였다.
## READ
- index 템플릿과 detail 템플릿에서 각 게시글의 작성자를 출력하도록 하였다.
---
# 댓글(COMMENT) 기능
## 모델 관계 설정
### Comment - Movie
- 0개 이상의 댓글은 1개의 게시글에 작성 될 수 있다. (N:1)
    - 댓글을 담당할 Comment 모델은 N, Movie 모델은 1
- Comment - Movie 모델의 N:1 관계를 설정하기 위해 `ForeignKey` 클래스를 이용하여 Comment 모델에 Movie 모델을 참조하는 외래키를 작성하였다.
    - 외래키가 참조하는 객체가 사라졌을 때 이를 참조하는 객체도 삭제하기 위해 on_delete 옵션 값을 CASCADE로 설정해주었다.
### Comment - User
- 0개 이상의 댓글은 1개의 회원에 의해 작성될 수 있다. (N:1)
    - 댓글을 담당할 Comment 모델은 N, User 모델은 1 
- Comment - User 모델의 N:1 관계를 설정하기 위해 `ForeignKey` 클래스를 이용하여 Comment 모델에 User 모델을 참조하는 외래키를 작성하였다.
    - 외래키가 참조하는 객체가 사라졌을 때 이를 참조하는 객체도 삭제하기 위해 on_delete 옵션 값을 CASCADE로 설정해주었다.
## Comment Create
- 사용자로부터 댓글 데이터를 입력하기 위해 ModelForm을 사용하여 CommentForm을 작성하였다.
- 댓글폼에서 외래키 필드는 보이지 않게 하기 위해 필드를 content만 출력하도록 설정하였다.
    - 출력에서 제외한 외래키는 variable routing을 사용하여 받을 수 있도록 하였다.
- 인증된 사용자인 경우만 댓글을 작성할 수 있도록 `is_authenticated`와 `view decorator`를 활용하여 함수를 작성하였다. 
    - 만약 인증되지 않은 사용자가 댓글을 작성할 경우 로그인 페이지로 이동하도록 하였다.
- 아직 데이터베이스에 저장되지 않은 인스턴스를 반환하기 위해 `save`메서드를 사용하여 함수를 작성하였다.
    - commit 옵션(commit=False)을 통해 DB에 저장되기 전 movie 객체를 저장하도록 하였다.
    - save의 commit 옵선을 활용하여 댓글 작성시 작성자 정보가 함께 저장될 수 있도록 하였다. (`comment.user = request.user`)
- detail 함수에서 특정 movie의 모든 댓글을 가져오기 위해 `comment_set manager`를 사용하였다.
## Comment delete
- 함수 작성시 댓글 삭제를 요청하려는 사람과 댓글을 작성한 사람을 비교하여 본인의 댓글만 삭제할 수 있도록 하였다.
    - 추가로 해당 댓글의 작성자가 아니라면, detail 페이지에서 if 태그를 활용하여 댓글 삭제 버튼을 출력하지 않도록 하였다.
- 인증된 사용자인 경우만 댓글을 삭제할 수 있도록 `is_authenticated`와 `view decorator`를 활용하였다. 
## 추가 구현
- 댓글이 없는 경우 대체 컨텐츠를 출력하기 위해 empty 태그를 사용하였다.
- detail 템플릿에서 댓글의 내용과 함께 각 댓글의 작성자도 출력하도록 하였다. 
---
# 좋아요(LIKE) 기능
## 모델 관계 설정
- Movie 모델에 `ManyToManyField`를 활용하여 user 모델과 M:N 관계를 갖는 like_users라는 필드를 추가하였다.
    - Movie-User에서 이미 User 모델을 참조하고 있기 때문에 user가 작성한 글들과 user과 좋아요를 누른 글을 구분하기 위해 ManyToManyField에 `related_name`을 작성하였다.
## like
- `.exists()` 메서드를 활용하여 버튼을 누른 유저가 like_users에 존재하면 해당 유저를 제거하고, 그렇지 않으면 추가하도록 함수를 작성하였다. 
- index 템플릿에서도 좋아요 유무에 따라 다른 버튼을 출력하도록 if 태그를 활용해 템플릿을 작성하였다.
- 인증된 사용자만 좋아요/좋아요 취소 버튼을 누를 수 있도록 `is_authenticated`와 `view decorator`를 활용하였다. 
    - 만약 인증되지 않은 사용자가 버튼을 누를 경우 로그인 페이지로 이동하도록 하였다.
---
# 팔로우(Follow) 기능
## profile 페이지 작성
- follow 기능 구현을 위해 프로필 페이지를 작성하였다.
- 프로필 템플릿으로 이동할 수 있도록 아래 페이지에 하이퍼 링크를 작성하였다.
    - index 페이지 - 작성자 이름
    - detail 페이지 - 작성자 이름
    - base 페이지 - nav 바
## 모델 관계 설정
- User 모델에 `ManyToManyField`를 활용하여 user 모델(self)과 M:N 관계를 갖도록 설정해주었다.
    - from_user_id 에서 to_user_id로 비대칭 재귀 참조를 하기 위해서 `symmetrical=False` 옵션을 지정해 주었다.
    - 역참조시 followers라는 이름으로 접근하도록 `related_name` 옵션을 지정해주었다.
## follow
- 프로필 유저와 request 유저가 다를 경우 팔로우/팔로우 취소 요청을 할 수 있도록 함수를 작성하였다.
    - 프로필 페이지에서도 프로필 유저와 request 유저가 다를 경우만 팔로우/언팔로우 버튼을 출력하도록 if 태그를 활용하여 템플릿을 작성하였다.
    - `.exists()` 메서드를 활용하여 버튼을 누른 유저가 followers에 존재하면 해당 유저를 제거하고, 그렇지 않으면 추가하도록 함수를 작성하였다. 
    - 프로필 페이지에 팔로우 유무에 따라 다른 버튼을 출력하도록 if 태그를 활용해 템플릿을 작성하였다.
- 프로필 페이지에 프로필 유저의 팔로잉, 팔로워 수를 출력하도록 DTL fliter인 `length`를 사용하였다. 