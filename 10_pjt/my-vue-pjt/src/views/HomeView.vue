<template>
  <div>
    <video autoplay muted loop>
      <source src="../assets/Network.mp4" type="video/mp4" />
    </video>
    <div class="intro-text-container">
      <h1 class="title">Save your Video in MyTube</h1>
      <h2 class="sub-title">무료 동영상 저장 서비스</h2>
      <div class="buttons-container">
        <router-link to="/search">
          <button type="button" class="btn btn-primary">동영상 검색</button>
        </router-link>
        <router-link to="/later">
          <button type="button" class="btn btn-warning">
            나중에 볼 동영상
          </button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
video {
  width: 100vw;
}
.intro-text-container {
  position: absolute;
  top: 0;
  height: 100vh;
  width: 100vw;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.title,
.sub-title {
  color: white;
}
.title {
  font-weight: bold;
}
.sub-title {
  margin-top: 30px;
}
.buttons-container {
  width: 350px;
  display: flex;
  margin-top: 30px;
  justify-content: space-between;
}
button {
  width: 140px;
}
</style>