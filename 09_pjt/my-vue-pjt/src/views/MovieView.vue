<template>
  <div class="container">
    <div class="row row-cols-1 row-cols-md-3 g-4">
      <MovieCard v-for="movie in movies" :key="movie.id" :movie="movie"/>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'

export default {
    name: 'MovieView',
    components: {
      MovieCard,
    },
    created() {
      this.getMovies()
    },
    methods: {
      getMovies() {
        this.$store.dispatch('getMovies')
      }
    },
    computed: {
      movies() {
        return this.$store.state.movies
      }
    }

}
</script>

<style>

</style>