import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const API_URL = 'https://api.themoviedb.org/3/movie/top_rated/'
const API_KEY = 'API_KEY'

export default new Vuex.Store({
  state: {
    movies : [],
    watchList : [],
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    CREATE_MOVIE(state, movieTitle) {
      state.watchList.push(movieTitle)
    },
    DELETE_MOVIE(state, movieTitle) {
      const index = state.watchList.indexOf(movieTitle)
      state.watchList.splice(index, 1)
    },
    UPDATE_MOVIE(state, movieTitle){
      state.watchList = state.watchList.map((movie) => {
        if (movie === movieTitle){
          movie.isCompleted = !movie.isCompleted
        }
        return movie
      })
    },
    LOAD_MOVIES(state){
      const localStorageMovies = localStorage.getItem('watchList')
      const parsedMovies = JSON.parse(localStorageMovies)

      state.watchList = parsedMovies ? parsedMovies : []
    }
  },
  getters: {
    getRandomMovie(state) {
      const randomIndex = Math.floor(Math.random() * state.movies.length)
      return state.movies[randomIndex]
    },
    watchListCount(state) {
      return state.watchList.length
    },
    completedMoviesCount(state) {
      const completedMovies = state.watchList.filter((movie) =>{
        return movie.isCompleted === true
      })
      return completedMovies.length
    }
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}?api_key=${API_KEY}&language=ko`
      }) 
        .then(res =>
          // console.log(res)
          context.commit('GET_MOVIES', res.data.results)
        )
        .catch(err => console.log(err))
    },
    createMovie(context, movieTitle){
      const movieItem = {
        title : movieTitle,
        isCompleted: false
      }
      context.commit('CREATE_MOVIE', movieItem)
      context.dispatch('saveToLocalStorage')
    },
    deleteMovie(context, movieTitle){
      context.commit('DELETE_MOVIE', movieTitle)
      context.dispatch('saveToLocalStorage')
    },
    updateMovie(context, movieTitle){
      context.commit('UPDATE_MOVIE', movieTitle)
      context.dispatch('saveToLocalStorage')
    },
    saveToLocalStorage(context){
      const jsonMovies = JSON.stringify(context.state.watchList)
      localStorage.setItem('watchList', jsonMovies)
    },
    loadMovies(context){
      context.commit('LOAD_MOVIES')
    }
  },
  modules: {
  }
})
