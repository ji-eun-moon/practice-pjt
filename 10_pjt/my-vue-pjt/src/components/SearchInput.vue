<template>
  <div>
    <div class="input-group">
      <input
        type="text"
        class="form-control"
        placeholder="검색어를 입력하세요"
        v-model="userInput"
        v-on:keyup.enter="getSearchData"
      />
      <button class="btn btn-success" type="button" v-on:click="getSearchData">
        찾기
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userInput: "",
    };
  },
  methods: {
    getSearchData() {
      this.$store.dispatch("getVideos", this.userInput);
      this.userInput = "";
    },
  },
};
</script>
