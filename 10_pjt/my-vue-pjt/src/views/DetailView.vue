<template>
  <div class="detail-view">
    <LoadingIcon v-if="isLoading" />
    <div v-else>
      <ArrowBack />
      <h1>{{ title }}</h1>
      <div class="upload-date">업로드 날짜: {{ publishedAt }}</div>
      <iframe
        width="560"
        height="315"
        :src="videoSrc"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
      ></iframe>
      <p class="description">{{ description }}</p>
      <button
        v-if="isLaterVideo"
        type="button"
        class="btn btn-danger"
        v-on:click="unregisterLaterVideo"
      >
        저장 취소
      </button>
      <button
        v-else
        type="button"
        class="btn btn-primary"
        v-on:click="registerLaterVideo"
      >
        동영상 저장
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import dayjs from "dayjs";
import ArrowBack from "@/components/common/ArrowBack.vue";
import LoadingIcon from "@/components/common/LoadingIcon.vue";
export default {
  components: {
    ArrowBack,
    LoadingIcon,
  },
  data() {
    return {
      video: {},
      isLaterVideo: null,
    };
  },
  computed: {
    isLoading() {
      return this.$store.state.loading;
    },
    title() {
      return this.video.title;
    },
    videoSrc() {
      return `https://www.youtube.com/embed/${this.video.videoId}?autoplay=1`;
    },
    description() {
      return this.video.description;
    },
    publishedAt() {
      return this.video.publishedAt;
    },
  },
  created() {
    this.$store.dispatch("changeLoading", true);
    axios
      .get(`${this.$store.state.URL}/videos`, {
        params: {
          key: this.$store.state.KEY,
          part: "snippet",
          id: this.$route.params.videoId,
        },
      })
      .then((response) => {
        const item = response.data.items[0];
        this.video = {
          videoId: item.id,
          title: item.snippet.title,
          description: item.snippet.description,
          publishedAt: dayjs(item.snippet.publishedAt).format("YYYY-MM-DD"),
        };
        this.isLaterVideo = this.checkVideoInStorage();
        this.$store.dispatch("changeLoading", false);
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {
    registerLaterVideo() {
      const listString = localStorage.getItem("laterVideoList");
      if (listString === null) {
        localStorage.setItem(
          "laterVideoList",
          `{"arr": ["${this.video.videoId}"]}`
        );
      } else {
        const laterVideoList = JSON.parse(listString);
        laterVideoList.arr.push(this.video.videoId);
        localStorage.setItem("laterVideoList", JSON.stringify(laterVideoList));
      }
      this.isLaterVideo = true;
    },
    unregisterLaterVideo() {
      const listString = localStorage.getItem("laterVideoList");
      const laterVideoList = JSON.parse(listString);
      const idx = laterVideoList.arr.indexOf(this.video.videoId);
      laterVideoList.arr.splice(idx, 1);
      localStorage.setItem("laterVideoList", JSON.stringify(laterVideoList));
      this.isLaterVideo = false;
    },
    checkVideoInStorage() {
      const listString = localStorage.getItem("laterVideoList");
      if (listString === null) {
        return false;
      }
      const laterVideoList = JSON.parse(listString);
      if (laterVideoList.arr.includes(this.video.videoId)) {
        return true;
      } else {
        return false;
      }
    },
  },
};
</script>

<style scoped>
.loading-icon-container {
  height: 80vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
}
h1 {
  margin-top: 20px;
  margin-bottom: 20px;
  font-weight: bold;
}
.upload-date {
  margin-bottom: 20px;
}
.description {
  margin-top: 20px;
}
</style>
