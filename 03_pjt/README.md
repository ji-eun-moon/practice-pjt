# 230317 3차 관통 프로젝트

---

## 프로젝트 목표

- HTML을 통한 웹 페이지 마크업 이해
  
- CSS 라이브러리의 이해와 활용
  
- Bootstrap 컴포넌트 및 Grid system을 활용한 반응형 레이아웃 구성
  

---

## 01_nav_footer.html

### 요구사항

- Navigation Bar
  - Bootstrap Navbar Component를 참고합니다.
  - 스크롤을 하더라도 항상 화면 상단에 고정되어 있습니다.
  - 로고 이미지는 제공된 logo.png를 사용합니다.
  - 로고 이미지는 하이퍼링크 역할을 하며, 클릭 시 02_home.html로 이동해야 합니다.
  - 내비게이션 메뉴 중 Home, Community는 하이퍼링크 역할을 하며,
    클릭 시 각각 02_home.html, 03_community.html로 이동해야 합니다.
  - 내비게이션 메뉴 중 Login은 클릭 시 Bootstrap Modal Component가 나타납니다.
  - Modal Component 내부에는 HTML form 요소를 배치합니다.
    - Bootstrap Forms Component를 참고합니다.
  - Viewport의 가로 크기 별 반응형 디자인은 스크린 샷 예시를 참고하여 일치하도록 합니다.
    
- Footer
  - 스크롤을 하더라도 항상 화면 하단에 고정되어 있습니다.
  - Footer에 작성된 내용은 수직·수평 가운데 정렬되어 있습니다.
    

### Discussion

- Footer position을 relative로 하였더니 스크롤을 위로 올리면 사라졌다.
  - position을 fixed로 바꾸어서 해결하였다.
- 마찬가지로 네비게이션 바도 위치를 고정하기 위해 fixed-top를 해주었다.
  
---

## 02_home.html

### 요구사항

- Header
  - Bootstrap Carousel Component로 구성합니다.
  - 이미지는 최소 3장 이상 사용하며 자동으로 전환됩니다.
    - 제공된 이미지를 사용합니다.
      
- Section
  - Section 내부의 개별 요소(article)들은 Bootstrap Card Component로 구성합니다.
    - 이미지, 제목, 설명을 포함합니다.
    - 이미지는 제공된 영화 포스터 이미지를 사용합니다.
  - 개별 요소들은 좌우 일정한 간격을 가집니다. (간격은 자유롭게 설정 가능)
  - Viewport의 가로 크기가 576px 미만일 경우 한 행에 1개씩 표시됩니다.
  - Viewport의 가로 크기가 576px 이상일 경우 한 행에 2개 이상 표시됩니다. 
    (자유롭게 설정 가능)
  - Viewport의 가로 크기 별 반응형 디자인은 스크린 샷 예시를 참고하여 일치하도록
    합니다.

### Discussion
- modal 코드를 nav 안에 작성하였더니 modal 창이 뜨지 않았다.
    - modal 코드를 nav 밖으로 꺼내서 해결하였다. 
- 하단에 고정한 footer가 section 내부를 침범하였다.
    - 02_home.html에 section padding, top을 설정하여 해결하였다.
- nav 를 fixed-top을 해주었더니 네비게이션 바가 아래 이미지와 겹치는 현상이 발생하였다.
  - body에 padding을 주어 해결하였다. 

---
## 03_community.html
### 요구사항
- Aside (게시판 목록)
    - HTML aside 요소로 이루어져 있습니다.
    - Bootstrap List Group Component로 구성합니다.
    - 내부의 각 항목은 클릭이 가능한 하이퍼링크이지만, URL은 별도로 없습니다.
    - Viewport의 가로 크기가 992px 미만일 경우 HTML main 요소 영역 전체만큼의 너비를 가집니다.
    - Viewport의 가로 크기가 992px 이상일 경우 HTML main 요소 영역 기준으로 좌측 1/6 만큼의 너비를 가집니다.
    - Viewport의 가로 크기 별 반응형 디자인은 스크린 샷 예시를 참고하여 일치하도록 합니다.
- Section (게시판)
    - 게시판은 HTML section 요소로 이루어져 있습니다.
    - 게시판은 Viewport의 가로 크기에 따라 전혀 다른 요소를 표시합니다.
        - Viewport의 가로 크기가 992px 미만일 경우 게시판은 HTML article 요소의 집합으로 표시되며, HTML main 요소 영역 전체만큼의 너비를 가집니다.
    - Viewport의 가로 크기가 992px 이상일 경우 게시판은 Bootstrap Tables Content로 구성되며, HTML main 요소 영역 기준으로 우측 5/6 만큼의 너비를 가집니다.
### Discussion
- 992px 이상에서 게시판 목록과 게시판 table이 수평으로 나열되어야 하는데 수직으로 나열 되는 현상이 발생하였다.
    - row 설정을 해주었더라도 게시판 목록과 table이 형제이어야 row 배열이 된다.
    - 처음에 col-lg-10 를 table의 div 태그에 해주었었는데, 전체 감싸고 있는 section 태그에 해주었더니 해결하였다.
- d-none/d-block 속성을 통해 화면 크기에 따라 항목을 사라지게 할 수 있다는 점을 알게 되었다. 
---
