<template lang="html">
  <!-- eslint-disable-next-line -->
  <div class="title"  @click="updateImg();">2D Render</div>
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
  align-items: center;
  width: 100%;
  padding-top: 10px;
}

.render {
  width: 415px;
}
</style>
