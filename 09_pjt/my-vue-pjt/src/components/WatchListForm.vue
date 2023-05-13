<template>
  <div>
    <input type="text" v-model.trim="movieTitle" @keyup.enter="createMovie">
    <button class="btn btn-dark ms-2" @click="createMovie">ADD</button>
  </div>
</template>

<script>
export default {
  name: 'WatchListForm',
  data() {
    return {
      movieTitle: null
    }
  },
  methods: {
    createMovie() {
      if (this.movieTitle) {
        this.$store.dispatch('createMovie', this.movieTitle)
      } else {
        alert('영화 제목을 입력하세요!')
      }
      this.movieTitle = null
    }
  }
}
</script>

<style>

</style>