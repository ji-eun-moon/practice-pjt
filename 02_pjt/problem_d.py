import requests
from pprint import pprint


def recommendation(title):
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

    # 영화 추천 목록 - URL 정보 설정
    path = 'movie/'+ movie_id + '/recommendations'

    pr_movie = {
        'api_key' : 'ec7cb21d2c86952874cdb3ff92cd1dfd',
        'language' : 'ko',
    }

    response = requests.get(BASE_URL+path, params=pr_movie).json()
    results = response.get('results')

    if len(results) == 0:  # 추천 영화가 없으면 [] 반환
        return []

    recommend = []

    for i in range(len(results)):
        recommend.append(results[i]['title'])
    return recommend

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
