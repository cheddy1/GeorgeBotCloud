<template>
  <div class="container-fluid no-mp">
    <div class="row no-mp">
      <div class="col no-mp">
        <div class="top-left box">
          <RenderMap/>
          <div class="loading-text">Waiting on render...</div>
        </div>
      </div>
      <div class="col no-mp">
        <div class="top-right box">
          <LiveFeed/>
        </div>
      </div>
    </div>
    <div class="row no-mp">
      <div class="col no-mp">
        <div class="bot-left box">
          <div class="loading-text"> Waiting on webcam data...</div>
        </div>
      </div>
      <div class="col no-mp">
        <div class="bot-right box">
          <div class="loading-text">Waiting on control data...</div>
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
.top-right {
  border-left: 0px;
  border-bottom: 2px;
  border-right: 0px;
  border-top: 0px;
  overflow: auto;
}

.top-left {
  border-left: 0px;
  border-bottom: 2px;
  border-right: 2px;
  border-top: 0px;
}

.bot-right {
  border: 0px;
  width: 50%;
  position: absolute;
  bottom: 0px;
}

.bot-left {
  width: 50%;
  border-left: 0px;
  border-bottom: 0px;
  border-right: 2px;
  border-top: 0px;
  position: absolute;
  bottom: 0px;
}

.feed-title {
  font-size: 20px;
  color: whitesmoke;
}

.box {
  height: 46vh;
  border-color: #494949;
  border-style: solid;
}

.no-mp {
  margin: 0 !important;
  padding: 0 !important;
}

.loading-text {
  display: flex;
  width: 100%;
  height: 100%;
  margin: auto;
  align-items: center;
  justify-content: center;
  color: #7393B3;
  opacity: 70%;
  font-size: 22px;
}
</style>
