<template>
  <div>
    <router-link class="arrow-back-container" to="/">
      <span class="arrow-back-icon material-symbols-outlined">
        arrow_back
      </span>
      <span class="arrow-back-text">뒤로가기</span>
    </router-link>
  </div>
</template>

<style scoped>
.arrow-back-container {
  display: flex;
  align-items: center;
  text-decoration-line: none;
  color: black;
  width: 100px;
}
.arrow-back-container:hover {
  color: blue;
  font-weight: bold;
}
.arrow-back-text {
  font-size: 1.2rem;
}
</style>
