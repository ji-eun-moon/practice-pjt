<template>
  <div class="col">
    <div class="card h-100 shadow">
      <img :src="'https://image.tmdb.org/t/p/original' + movie.poster_path" alt="poster">
      <div class="card-body d-flex flex-column">
        <h3 class="card-title text-center">{{ movie.title }}</h3>
        <br>
        <div class="icon-text justify-content-end">
          <i class="bi bi-star-fill ic-yellow me-2"></i>
          <p class="content">평점 : {{ movie.vote_average }}</p>
        </div>
        <p class="overview">{{ movie.overview }}</p>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'MovieCard',
  props: {
    movie: Object
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;400;600&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@700&display=swap');

.overview {
  white-space: normal;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  overflow: hidden;
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 400;
}

.card-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 700;
}

.content {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 600;
}

.icon-text {
  display: flex;
}

.ic-yellow {
  color: #FBBF24;
}
</style>