import json


def dec_movies(movies):
    pass 
    # 여기에 코드를 작성합니다.
    lst = []
    for movie in movies:
        
        # 파일 열기
        id = movie.get('id')
        movie_json = open(f'data/movies/{id}.json', encoding='utf-8')
        movie_detail = json.load(movie_json)

        # 개봉일이 12월인지 확인
        if movie_detail['release_date'][5:7] == '12':
            lst.append(movie_detail['title'])
        
    return lst

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
