<template>
  <div>
    <ul class="video-list-ul">
      <li
        class="video-list-li"
        v-for="video in laterVideoList"
        v-bind:key="video.videoId"
      >
        <EachVideo v-bind:video="video" />
      </li>
    </ul>
  </div>
</template>

<script>
import EachVideo from "@/components/common/EachVideo.vue";
export default {
  components: {
    EachVideo,
  },
  props: {
    laterVideoList: Array,
  },
};
</script>
