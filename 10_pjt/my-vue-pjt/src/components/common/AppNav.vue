<template>
<div>
    <nav class="navbar fixed-top bg-dark navbar-expand-lg bg-body-tertiary" data-bs-theme="dark">
        <div class="container-fluid">
            <router-link class="navbar-brand" to="/">MyTube</router-link> 
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav"> 
                        <li class="nav-item">
                        <router-link class="nav-link" to="/">Home</router-link> </li>
                        <li class="nav-item">
                        <router-link class="nav-link" to="/search">Search</router-link>
                        </li>
                        <li class="nav-item">
                        <router-link class="nav-link" to="/later">Later</router-link>
                        </li>
                    </ul> 
            </div>
        </div>
    </nav>
</div> 
</template>

<script>
export default {

}
</script>

<style>

</style>