import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다. 
    result = []
    for i in range(len(movies_list)):
        dict = {
            'id' : movies_list[i].get('id'),
            'title' : movies_list[i].get('title'),
            'poster_path' : movies_list[i].get('poster_path'),
            'vote_overage' : movies_list[i].get('vote_average'),
            'overview' : movies_list[i].get('overview'),
            'genre_names' : movies_list[i].get('genre_ids')
        }
        
        for genre in genres_list:
            for i in range(len(dict['genre_names'])):
                if dict['genre_names'][i] == genre['id']:
                    dict['genre_names'][i] = genre['name']
                    
        result.append(dict)
    
    return result

        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
