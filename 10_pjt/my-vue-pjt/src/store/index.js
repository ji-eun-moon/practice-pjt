import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import dayjs from 'dayjs'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    videoList: [],
    loading: false,
    URL : "https://www.googleapis.com/youtube/v3",
    KEY : "API_KEY"

  },
  getters: {
  },
  mutations: {
    CHANGE_VIDEO_LIST(state, videoList) {
			state.videoList = videoList;
		},
    CHANGE_LOADING(state, flag){
      state.loading = flag
    }
  },
  actions: {
    getVideos(context, word) {
      axios.get(`${context.state.URL}/search`, {
        params: {
          key: context.state.KEY,
          part: "snippet",
          type: "video",
          q: word,
          maxResults: 10,
        },
      })
      .then((response) => {
        const parsedVideoList = response.data.items.map((item) => {
          return {
            videoId: item.id.videoId,
            title: item.snippet.title,
            description: item.snippet.description,
            publishTime: dayjs(item.snippet.publishTime).format("YYYY-MM-DD"),
            thumbnails: item.snippet.thumbnails,
          }
        })
        context.commit("CHANGE_VIDEO_LIST", parsedVideoList)
        context.dispatch("changeLoading", false)
      })
      .catch((error) => {
        console.log(error)
      })
    },
    changeLoading(context, flag){
      context.commit("CHANGE_LOADING", flag)
    }
  },
  modules: {
  }
})
