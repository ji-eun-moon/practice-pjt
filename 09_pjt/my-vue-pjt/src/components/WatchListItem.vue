<template>
  <div class="movie-item" @click="updateMovie">
      <i class="bi bi-film me-4 fs-3 mt-1"></i>
      <span class="content" :class="{ 'is-completed' : movie.isCompleted }">{{ movie.title }}</span>
      <button class="ms-auto btn btn-secondary" @click="deleteMovie">DELETE</button>
  </div>
</template>

<script>

export default {
  name:'WatchListItem',
  props: {
    movie: Object
  },
  methods: {
    deleteMovie() {
      this.$store.dispatch('deleteMovie', this.movie)
    },
    updateMovie() {
      this.$store.dispatch('updateMovie', this.movie)
    },
  },
}

</script>

<style>
.movie-item {
  margin: 1rem 0;
  padding: 1rem;
  display: flex;
  align-items: center;
  border: 1px solid #D1D5DB;
  border-radius: .5rem;
  cursor: pointer;
}

.is-completed {
  text-decoration: line-through;
  color: gray;
}
</style>