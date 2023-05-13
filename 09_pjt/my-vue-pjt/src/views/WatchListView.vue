<template>
  <div class="container">
    <div class="watch-list-form">
      <h1 class="content">보고싶은 영화</h1>
      <h5 class="content">총 {{ watchListCount }} 개</h5>
      <WatchListForm />
    </div>
    <br>
      <div class="completed-movies-section">
      <div class="completed-movies-count">
        <h6 class="content me-3 mt-1">본 영화 : {{ completedMoviesCount }} 개</h6>
      </div>
      <div class="completed-movies-delete">
        <button class="btn btn-outline-secondary btn-sm" @click="deleteCompletedMovies">본 영화 전부 삭제하기</button>
      </div>
    </div>
    <WatchListItem v-for="(movie, index) in watchList" :key="index" :movie="movie" />
  </div>
</template>

<script>
import WatchListItem from '@/components/WatchListItem.vue'
import WatchListForm from '@/components/WatchListForm.vue'

export default {
  name: 'WatchListView',
  components: {
    WatchListItem,
    WatchListForm
  },
  created() {
    this.$store.dispatch('loadMovies')
  },
  computed: {
    watchList() {
      return this.$store.state.watchList
    },
    watchListCount() {
      return this.$store.getters.watchListCount
    },
    completedMoviesCount() {
      return this.$store.getters.completedMoviesCount
    }
  },
  methods: {
    deleteCompletedMovies() {
      const completedMovies = this.watchList.filter((movie) => {
        return movie.isCompleted === true
      })
      completedMovies.forEach((movie) => {
        this.$store.dispatch('deleteMovie', movie)
      })
    }
  }

}
</script>

<style>

.watch-list-form {
  background-color : #d2eddd;
  height: 200px;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.completed-movies-section {
  display: flex;
  justify-content: flex-end;
}

</style>