<template>
  <div class="later-view">
    <ArrowBack />
    <h1>나중에 볼 동영상</h1>
    <LoadingIcon v-if="isLoading" />
    <div v-else>
      <div v-if="isLaterVideo">
        <LaterVideoList v-bind:laterVideoList="laterVideoList" />
      </div>
      <div v-else>등록된 비디오 없음</div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import dayjs from "dayjs";
import LaterVideoList from "../components/LaterVideoList.vue";
import ArrowBack from "../components/common/ArrowBack.vue";
import LoadingIcon from "../components/common/LoadingIcon.vue";
export default {
  components: {
    LaterVideoList,
    ArrowBack,
    LoadingIcon,
  },
  data() {
    return {
      isLaterVideo: null,
      laterVideoList: [],
    };
  },
  computed: {
    isLoading() {
      return this.$store.state.loading;
    }
  },
  created() {
    this.$store.dispatch("changeLoading", true);
    const listString = localStorage.getItem("laterVideoList");
    if (listString === null) {
      this.$store.dispatch("changeLoading", false);
      return;
    }
    const laterVideoList = JSON.parse(listString);
    if (laterVideoList.arr.length === 0) {
      this.$store.dispatch("changeLoading", false);
      return;
    }
    this.setLaterVideoList(laterVideoList.arr);
    this.isLaterVideo = true;
    this.$store.dispatch("changeLoading", false);
  },
  methods: {
    setLaterVideoList(videoIds) {
      videoIds.forEach((videoId) => {
        axios
          .get(`${this.$store.state.URL}/videos`, {
            params: {
              key: this.$store.state.KEY,
              part: "snippet",
              id: videoId,
            },
          })
          .then((response) => {
            const data = response.data.items[0];
            this.laterVideoList.push({
              videoId: data.id,
              title: data.snippet.title,
              description: data.snippet.description,
              publishTime: dayjs(data.snippet.publishedAt).format("YYYY-MM-DD"),
              thumbnails: data.snippet.thumbnails,
              channelId: data.snippet.channelId,
            });
          })
          .catch((error) => {
            console.log(error);
          });
      });
    },
  },
};
</script>

<style scoped>
h1 {
  margin-top: 20px;
  margin-bottom: 20px;
  font-weight: bold;
}
.loading-icon-container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 80vh;
}
</style>
