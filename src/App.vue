<template>
  <b-navbar class="nav" toggleable="lg" variant="" >
    <b-navbar-brand style="color: white;" href="#">
      <img alt="george logo" style="width: 5vh; padding-right: 5px;" src="./assets/logo.png">
      Welcome to GeorgeBot!
    </b-navbar-brand>
  </b-navbar>
  <router-view/>
</template>

<style>
#app {
  color: whitesmoke;
  height: 100vh;
  background-color: #212121;
}

.nav {
  height: 8vh;
  background-color: #494949;
}

</style>
