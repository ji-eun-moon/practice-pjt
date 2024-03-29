import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다. 
    dict = {
        'id' : movie.get('id'),
        'title' : movie.get('title'),
        'poster_path' : movie.get('poster_path'),
        'vote_overage' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_names' : movie.get('genre_ids')
    }
    
    for genre in genres_list:
        for i in range(len(dict['genre_names'])):
            if dict['genre_names'][i] == genre['id']:
                dict['genre_names'][i] = genre['name']
    
    return dict
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
