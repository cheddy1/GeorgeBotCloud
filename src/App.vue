<template>
  <b-navbar class="nav" toggleable="lg" variant="" style="">
    <b-navbar-brand style="color: whitesmoke;" to="/">
      <img alt="george logo" style="width: 5vh; padding-right: 5px;" src="./assets/logo.png">
      Welcome to GeorgeBot!
    </b-navbar-brand>
    <b-navbar-nav align="start" class="ml-auto">
      <b-nav-item to="about">About</b-nav-item>
    </b-navbar-nav>
  </b-navbar>
  <router-view/>
</template>

<style>
#app {
  color: whitesmoke;
  height: 100vh;
  background-color: #323232;
}

.nav {
  height: 8vh;
  background-color: #4b4b4b;
}

nav .navbar-nav li a{
  margin-right: 1vw;
  color: whitesmoke !important;
}

</style>
