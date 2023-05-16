<template>
  <div>
    <div
      class="video-card card text-bg-light border-secondary"
      v-on:click="moveToDetail"
    >
      <img
        class="card-img-top"
        v-bind:src="thumbnailSrc"
        v-on:click="moveToDetail"
        alt="video"
      />
      <div class="card-body">
        <p class="card-text">{{ title }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    video: {
      description: String,
      publishTime: String,
      thumbnails: {
        default: {
          height: Number,
          width: Number,
          url: String,
        },
        high: Object,
        medium: Object,
      },
      title: String,
      videoId: String,
    },
  },
  computed: {
    thumbnailSrc() {
      return this.video.thumbnails.medium.url;
    },
    detailUrl() {
      return `/videos/${this.video.videoId}`;
    },
    title() {
      return this.video.title;
    },
  },
  methods: {
    moveToDetail() {
      this.$router.push(`/videos/${this.video.videoId}`);
    },
  },
};
</script>

<style scoped>
.video-card {
  width: 300px;
  height: 300px;
}
.card-text {
  font-size: 1.2rem;
  font-weight: bolder;
}
</style>