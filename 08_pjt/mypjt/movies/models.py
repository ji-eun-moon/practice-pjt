from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)

    def get_similar_movies(self):
        # 1. 현재 영화 객체의 장르를 가져오기
        genres = self.genres.all()
        # 2. 가져온 장르를 가지고 다른 영화 객체를 찾기
        movies = Movie.objects.filter(genres__in=genres).exclude(id=self.id).distinct()
        # 3. 찾은 영화 객체들을 평점 기준으로 내림차순으로 정렬하기
        similar_movies = movies.order_by('-vote_average')
        return similar_movies
