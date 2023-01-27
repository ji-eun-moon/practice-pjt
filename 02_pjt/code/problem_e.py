import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    # 영화 검색 - URL 정보 설정
    BASE_URL = 'https://api.themoviedb.org/3/'
    path_search = 'search/movie'

    pr_search = {
        'api_key' : 'ec7cb21d2c86952874cdb3ff92cd1dfd',
        'language' : 'ko',
        'region' : 'KR',
        'query' : title
    }
    # 검색한 영화의 id 값 얻기 
    response = requests.get(BASE_URL+path_search, params=pr_search).json()
    search_results = response.get('results')

    if len(search_results) == 0:  # 검색한 영화정보가 없다면 None 반환
        return None
    
    movie_id = str(search_results[0]['id'])

    # 출연진, 스태프 조회 - URL 설정
    path = 'movie/'+ movie_id + '/credits'

    pr_movie = {
        'api_key' : 'ec7cb21d2c86952874cdb3ff92cd1dfd',
        'language' : 'ko',
    }

    response = requests.get(BASE_URL+path, params=pr_movie).json()
    cast = response.get('cast')
    crew = response.get('crew')

    cast_lst = []  
    crew_lst = []  
    
    # cast_id가 10 미만인 출연진만 추출
    for i in range(len(cast)):
        if cast[i]['cast_id'] < 10:
            cast_lst.append(cast[i]['name'])

    # department가 Directing인 스태프만 추출
    for i in range(len(crew)):
        if crew[i]['department'] == 'Directing':
            crew_lst.append(crew[i]['name'])

    # 추출한 출연진, 연출진 딕셔너리
    credits_dic = { 'cast' : cast_lst, 'directing' : crew_lst }

    return credits_dic

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
