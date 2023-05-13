<template>
  <!-- <div id="app">
    <nav>
      <router-link :to="{ name: 'movies' }">Movie</router-link> |
      <router-link :to="{ name: 'random' }">Random</router-link> |
      <router-link :to="{ name: 'watch-list'}">WatchList</router-link>
    </nav>
    <router-view/>
  </div> -->
  <div id="app">
    <nav class="navbar navbar-expand-md navbar-dark bg-success mb-4">
      <i class="bi bi-camera-reels fs-2 me-3 film"></i>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link :to="{ name: 'movies' }" class="nav-link">Movie</router-link>
          </li>
          <li class="nav-item">
            <router-link :to="{ name: 'random' }" class="nav-link">Random</router-link>
          </li>
          <li class="nav-item">
            <router-link :to="{ name: 'watch-list'}" class="nav-link">WatchList</router-link>
          </li>
        </ul>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

.nav-link.router-link-active {
  color: #105d2c !important;
}

.film {
  color: whitesmoke;
}
</style>
