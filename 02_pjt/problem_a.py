import requests

# ec7cb21d2c86952874cdb3ff92cd1dfd

def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    
    # url 정보 설정하기 
    # 방법 1
    # URL = 'https://api.themoviedb.org/3/movie/popular?api_key=ec7cb21d2c86952874cdb3ff92cd1dfd&language=ko&page=1&region=KR'
    # 방법 2
    BASE_URL = 'https://api.themoviedb.org/3/'
    path = 'movie/popular'

    pr = {
        'api_key' : 'ec7cb21d2c86952874cdb3ff92cd1dfd',
        'language' : 'ko',
        'region' : 'KR'
    }

    # 요청하고 응답하기
    response = requests.get(BASE_URL+path, params=pr).json()
    result = response.get('results')

    # 결과 리턴하기 (영화 개수 계산)
    return len(result)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
