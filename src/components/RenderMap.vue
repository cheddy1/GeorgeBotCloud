<template lang="html">
  <!-- eslint-disable-next-line -->
  <div class="title" style="padding-top: 9px;" @click="checkIntervalHandler();">2D Render</div>
  <div class="render-box">
    <!-- eslint-disable-next-line -->
    <img @click="checkIntervalHandler();" alt="render" class="render" :src="imageUrl">
  </div>
</template>

<script lang="js">

const baseUrl = process.env.NODE_ENV === 'production' ? 'http://george-env.eba-trrm37cn.us-east-2.elasticbeanstalk.com/' : 'http://127.0.0.1:5000/';
const origUrl = `${baseUrl}api/2d-image`;
export default {
  name: 'render-map',
  props: [],
  mounted() {
  },
  data() {
    return {
      imageUrl: origUrl,
      interval: setInterval(this.updateImg, 5010),
      checkInterval: false,
    };
  },
  methods: {
    checkIntervalHandler() {
      if (this.checkInterval) {
        this.startUpdate();
        this.checkInterval = false;
      } else {
        this.stopUpdate();
        this.checkInterval = true;
      }
    },
    startUpdate() {
      this.interval = setInterval(this.updateImg, 5010);
    },
    stopUpdate() {
      clearInterval(this.interval);
    },
    updateImg() {
      this.imageUrl = `${origUrl}?cache=${Math.random()}`;
    },
  },
  computed: {
  },
};

</script>

<style scoped>

.render-box {
  display: flex;
  justify-content: center;
  padding: 20px;
  height: 100%;
  width: 100%;
}

.render {
  max-width: 80%;
  max-height: 94%;
}
</style>
