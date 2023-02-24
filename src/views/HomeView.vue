<template>
  <div class="container-fluid h-100">
    <div class="row h-100">
      <div class="col-7">
        <div class="row" style="margin-top: 3vh;">
          <div class="col-2">
            <img alt="george logo" style="width: 10vh;" src="../assets/logo.png">
          </div>
          <div class="col">
            Welcome to GeorgeBot
          </div>
        </div>
        <div class="render-box">
          <RenderMap/>
        </div>
      </div>
      <div class="col">
        <div class="feed-title">
          Data Feed
        </div>
        <div class="feed-box">
          <LiveFeed/>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
// @ is an alias to /src
import LiveFeed from '@/components/LiveFeed.vue';
import RenderMap from '@/components/RenderMap.vue';

export default {
  name: 'HomeView',
  components: {
    LiveFeed,
    RenderMap,
  },
};
</script>

<style>
.feed-box {
  margin-bottom: 8vh;
  margin-right: 3vw;
  height: 78vh;
  border: 2px;
  border-color: whitesmoke;
  border-style: solid;
  overflow: auto;
}

.feed-title {
  margin-top: 10vh;
  font-size: 20px;
  color: whitesmoke;
}
.render-box {
  /* margin-bottom: 8vh;
  margin-right: 3vw; */
  margin-top: 1vh;
  height: 75vh;
  border: 2px;
  border-color: whitesmoke;
  border-style: solid;
}
</style>
