import json  # json 형식의 파일을 파이썬 객체로 / 파이썬 객체를 json 형식으로 바꿀 때
from pprint import pprint  # 딕셔너리 출력시 키값을 오름차순으로 정렬해서 출력


def movie_info(movie):
    pass 
    # 여기에 코드를 작성합니다.
    
    dict = {
        'id' : movie_dict.get('id'),
        'title' : movie_dict.get('title'),
        'poster_path' : movie_dict.get('poster_path'),
        'vote_overage' : movie_dict.get('vote_average'),
        'overview' : movie_dict.get('overview'),
        'genre_ids' : movie_dict.get('genre_ids')
    }
    
    return dict
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')  
    # open(파일경로)
    # utf-8 : 유니코드를 가변형식으로 데이터를 읽는 방법
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
