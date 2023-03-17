import json


def max_revenue(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    # revenue_lst = []
    revenue_max = 0
    for movie in movies:

        id = movie.get('id')
        movie_json = open(f'data/movies/{id}.json', encoding='utf-8')
        movie_detail = json.load(movie_json)

    #     revenue_lst.append(movie_detail['revenue'])

    # revenue_max = revenue_lst[0]
    # for i in range(len(revenue_lst)):
    #     if revenue_lst[i] > revenue_max:
    #         revenue_max = revenue_lst[i]

    # for movie in movies:

    #     id = movie.get('id')
    #     movie_json = open(f'data/movies/{id}.json', encoding='utf-8')
    #     movie_detail = json.load(movie_json)

    #     if movie_detail['revenue'] == revenue_max:
    #         return movie_detail['title'] 
        
        if movie_detail['revenue'] > revenue_max:
            revenue_max = movie_detail['revenue']
            movie_title = movie_detail['title']
        
    return movie_title


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    
    print(max_revenue(movies_list))

