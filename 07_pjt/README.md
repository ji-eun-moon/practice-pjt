# 230421 관통 프로젝트 07 - DB 설계를 활용한 REST API 설계
## 프로젝트 목표
- DRF(Django Rest Framework)를 활용한 API Server 제작
- Database many to one relationship(1:N)에 대한 이해
- Database many to many relationship(M:N)에 대한 이해
# 구현 사항
## 전체 배우 목록 조회하기
- 전체 배우 목록을 조회하기 위한 `ActorListSerializer`을 작성하였다.
    - 출력할 field는 ('id', 'name')로 설정하였다.
## 단일 배우 정보 조회하기
- 단일 배우 정보를 조회하기 위한 `ActorSerializer`를 작성하였다.
    - 출력할 field는 `'__all__'`로 설정하였다.
- 단일 배우 정보를 조회할 때 단일 배우와 1:N 역참조 관계인 영화 정보(movie_set)를 함께 조회하도록 하였다.
    - 영화 정보 중에서 title만 가져오기 위해 field로 title만 포함하는 `MovieDetailSerializer`을 새로 작성하고 중첩 관계(Nested relationship)로 참조하였다.
    - Movie 역참조 명을 movie_set에서 movies로 변경하기 위해 Movie 모델에서 related_name을 movies로 설정해주었다.
## 전체 영화 목록 조회하기
- 전체 배우 목록을 조회하기 위한 `MovieListSerializer`을 작성하였다.
    - 출력할 field는 ('title', 'overview')로 설정하였다.
## 단일 영화 정보 조회하기
- 단일 영화 정보를 조회하기 위한 `MovieSerializer`를 작성하였다.
    - 출력할 field는 `'__all__'`로 설정하였다.
- 단일 영화 정보를 조회할 때 단일 배우와 1:N 정참조 관계인 배우 정보(actor)를 함께 조회하도록 하였다.
    - 배우 정보 중에서 name만 가져오기 위해 field로 name만 포함하는 `ActorDetailSerializer`를 새로 작성하고 중첩 관계(Nested relationship)로 참조하였다.
- 단일 영화 정보를 조회할 때 단일 배우와 1:N 역참조 관계인 리뷰 정보(review_set)를 함께 조회하도록 하였다.
    - 리뷰 정보 중에서 title과 content만 가져오기 위해 field로 title, content만 포함하는 `ReviewListSerializer`를 중첩 관계(Nested relationship)로 참조하였다.
## 전체 리뷰 목록 조회하기
- 전체 리뷰 목록을 조회하기 위한 `ReviewListSerializer`을 작성하였다.
    - 출력할 field는 ('title', 'content',)로 설정하였다.
## 단일 리뷰 조회 & 수정 & 삭제하기
- 단일 리뷰 정보를 조회/수정/삭제하기 위한 `ReviewSerializer`를 작성하였다.
    - 출력할 field는 `'__all__'`로 설정하였다.
    - 리뷰 수정 시 movie 필드를 유효성 검사에서 제외시키고 데이터 조회 시에만 출력하기 위해 read_only_fields를('movie',)로 설정해주었다.
- 리뷰 삭제 시 삭제 메시지를 출력하기 위해 review_detail 함수에서 삭제 메세지를 포함하는 data를 추가하였다.
    - 요청에 대한 데이터 삭제가 성공했을 경우에는 204 No Content 상태 코드를 응답하도록 하였다. 
- 리뷰 수정 시 유효성 검사 오류가 있는 경우 ValidationError 예외를 발생시키는 선택적 raise_exception 인자를 사용하였다. 
    - 요청에 대한 데이터 수정이 성공했을 경우는 200 OK 상태 코드 응답하도록 하였다.
## 리뷰 생성하기
- ReviewSerializer를 통해 Serializer되는 과정에서 Parameter로 넘어온 movie_pk에 해당하는 movie 객체를 추가적인 데이터로 넘겨 저장하기 위해 save()메서드를 사용하였다. 
## 추가 구현
- 모델 manager objects에서 객체를 불러올 때 해당 객체가 없을 땐 기존 DoesNotExist 예외 대신 Http404를 raise 할 수 있도록 `get_object_or_404`과 `get_list_or_404`를 사용하였다.