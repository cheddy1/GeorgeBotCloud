<template lang="html">
  <!-- eslint-disable-next-line -->
  <div class="title" style="padding-top: 7px;" @click="updateImg();">2D Render</div>
  <div class="render-box">
    <!-- eslint-disable-next-line -->
    <img @click="updateImg();" alt="render" class="render" :src="imageUrl">
  </div>
</template>

<script lang="js">

const baseUrl = process.env.NODE_ENV === 'production' ? 'http://george-env.eba-trrm37cn.us-east-2.elasticbeanstalk.com/' : 'http://127.0.0.1:5000/';
const origUrl = `${baseUrl}api/2d-image`;
export default {
  name: 'render-map',
  props: [],
  mounted() {
    // setInterval(this.updateImg, 1000);
  },
  data() {
    return {
      imageUrl: origUrl,
    };
  },
  methods: {
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
  height: 42vh;
  width: 100%;
}

.render {
  width: 600px;
  max-width: 80%;
  max-height: 97%;
}
</style>
