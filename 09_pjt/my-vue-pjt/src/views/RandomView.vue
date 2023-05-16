<template>
  <div class="container">
    <div class="card shadow justify-content-center m-5 random-card">
      <button class="btn pick-btn" @click="pickRandomMovie">PICK</button>
      <img :src="'https://image.tmdb.org/t/p/original' + randomMovie.poster_path" alt="poster">
      <div class="card-body">
        <h3 class="card-title">{{ randomMovie.title }}</h3>
        <div class="icon-text justify-content-end">
          <i class="bi bi-star-fill ic-yellow me-2"></i>
          <p class="content">평점 : {{ randomMovie.vote_average }}</p>
        </div>
        <p class="content">{{ randomMovie.overview }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'https://api.themoviedb.org/3/movie/top_rated/'
const API_KEY = 'API_KEY'

export default {
  name: 'RandomView',
  created() {
    this.getRandomMovie();
  },
  data() {
    return {
      randomMovie: null
    }
  },
  methods: {
    getRandomMovie() {
      axios({
        method: 'get',
        url: `${API_URL}?api_key=${API_KEY}&language=ko`
      }) 
        .then(res => {
          const movieData = res.data.results
          const randomIndex = Math.floor(Math.random() * movieData.length);
          this.randomMovie = movieData[randomIndex];
      })
        .catch(err => console.log(err))
    },
    pickRandomMovie() {
      this.getRandomMovie();
    }
  }
}
</script>

<style>
.pick-btn {
  background-color: #d2eddd;
  width: 100%;
  margin-bottom: 10px;
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 600;
  font-size: large;
  border-radius: 20px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}

.random-card {
  border-radius: 20px;
}
</style>