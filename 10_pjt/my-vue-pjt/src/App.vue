<template>
  <div id="app">
    <AppNav />
    <div class="page">
      <router-view/>
    </div>
  </div>
</template>

<script>
import AppNav from '@/components/common/AppNav.vue'

export default ({
  components: {
    AppNav,
  }
})
</script>


<style>
#app {
  font-family: "Noto Sans KR", sans-serif;
}
ul {
  padding-left: 0;
  list-style: none;
}
.page {
  padding-top: 3.5rem;
}

.search-view,
.later-view,
.detail-view {
  padding-left: 100px;
  padding-right: 100px;
}
.video-list-ul {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
}
.video-list-li {
  margin-bottom: 30px;
}
</style>
